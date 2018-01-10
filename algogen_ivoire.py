import random
from typing import List

from bobine_store import BobineStore, bobine_store, Bobine, get_combinaison_label
from bobine_mere_store import bobine_mere_store
from refente_store import refente_store
from model.prod import PlanProd, Production, Emplacement


class Stock:
    def __init__(self, bobine: Bobine, stock: int) -> None:
        self.bobine = bobine
        self.quantity = stock

    def __repr__(self):
        return "Stock {} : {}".format(self.bobine, self.quantity)


class StockStore:
    def __init__(self):
        self.stocks = []  # type: List[Stock]

    def add_stock(self, stock: Stock):
        self.stocks.append(stock)

    def add_bobine(self, bobine: Bobine, quantity: int):
        for stock in self.stocks:
            if stock.bobine is bobine:
                stock.quantity += quantity
                return
        self.add_stock(Stock(bobine, quantity))

    def __repr__(self):
        for stock in self.stocks:
            print(stock)
        return ""


class Individu:
    def __init__(self, plan_prod: PlanProd):
        self.plan_prod = plan_prod
        self.stock_store = self.get_stock_store()
        self.fitness = self.get_fitness()

    def get_stock_store(self):
        new_stock_store = StockStore()
        for prod in self.plan_prod.prods:
            for emplacement in prod.emplacements:
                quantity = emplacement.pose
                bobine = emplacement.bobine
                quantity = max(quantity, 1)
                new_stock_store.add_bobine(bobine, quantity)
        return new_stock_store

    def mutation(self):
        self.plan_prod.mutation()
        self.stock_store = self.get_stock_store()
        self.fitness = self.get_fitness()

    def get_fitness(self):
        fitness = 0
        for stock in self.stock_store.stocks:
            if stock.bobine.code == 403:
                fitness += stock.quantity
        return fitness

    def __repr__(self):
        for plan_prod in self.plan_prod.prods:
            print(plan_prod)
        return "Note: {} \n".format(self.fitness)


class Generation:
    def __init__(self,
                 plan_prod_size: int=None,
                 generation_size: int=None,
                 combinaisons: List[Production]=None,
                 mutation_rate: float=None):
        self.individus = []  # type: List[Individu]
        self.generation_size = generation_size
        self.plan_prod_size = plan_prod_size
        self.combinaisons = combinaisons
        self.mutation_rate = mutation_rate

    def get_individus(self):
        while len(self.individus) < self.generation_size:
            new_plan_prod = PlanProd(combinaisons=self.combinaisons)
            new_plan_prod.get_plan_production(self.plan_prod_size)
            self.individus.append(Individu(new_plan_prod))

    def add_individu(self, individu: Individu):
        self.individus.append(individu)

    def sort_individu(self):
        self.individus.sort(key=lambda i: i.fitness, reverse=True)

    def get_croissement(self, plan_prod_1: PlanProd, plan_prod_2: PlanProd) -> PlanProd:
        index_cut = random.randint(0, len(plan_prod_1.prods) - 1)
        new_plan_prod = PlanProd(self.combinaisons)
        while len(new_plan_prod.prods) < len(plan_prod_1.prods):
            plan_prod_parent = plan_prod_1 if len(new_plan_prod.prods) < index_cut else plan_prod_2
            new_plan_prod.prods.append(plan_prod_parent.prods[len(new_plan_prod.prods)])
        return new_plan_prod

    def get_next_generation(self):
        new_generation = Generation(generation_size=self.generation_size)
        new_generation.add_individu(self.individus[0])
        index_generation = 0
        while len(new_generation.individus) < self.generation_size:
            plan_prod_1 = self.individus[index_generation].plan_prod
            plan_prod_2 = self.individus[index_generation + 1].plan_prod
            new_plan_prod = self.get_croissement(plan_prod_1, plan_prod_2)
            new_individu = Individu(new_plan_prod)
            new_generation.add_individu(new_individu)
            new_plan_prod = self.get_croissement(plan_prod_2, plan_prod_1)
            new_individu = Individu(new_plan_prod)
            new_generation.add_individu(new_individu)
            index_generation += 1
        count_mutation = 0
        while count_mutation < round(len(new_generation.individus)*self.mutation_rate):
            alea_index = random.randint(0, len(new_generation.individus)-1)
            new_generation.individus[alea_index].mutation()
            count_mutation += 1
        new_generation.sort_individu()
        return new_generation

    def __repr__(self):
        for individu in self.individus:
            print(individu)
        return ""


def get_bobine_ivoire() -> BobineStore:
    bobine_store_ivoire = BobineStore()
    for bobine in bobine_store.bobines:
        if bobine.color == "ivoire":
            bobine_store_ivoire.add_bobine(bobine)
    return bobine_store_ivoire


def get_combinaison_from_bobine_store(current_bobine_store: BobineStore) -> List[Production]:
    combinaisons = []
    for bobine_mere in bobine_mere_store.bobines_meres:
        if bobine_mere.color != "ivoire":
            continue
        refentes = refente_store.filter_for_bobine_mere(bobine_mere).refentes
        for refente in refentes:
            new_bobine_store = current_bobine_store.filter_from_refente_and_bobine_mere(refente=refente,
                                                                                        bobine_mere=bobine_mere)
            new_combinaisons = new_bobine_store.get_combinaisons_from_refente(refente=refente)
            combinaisons += new_combinaisons
    dic_combinaisons = bobine_store.dedupe_combinaisons(combinaisons)
    combinaisons = []
    for combinaison in dic_combinaisons:
        combinaisons.append(combinaison)
    return combinaisons


def display_combinaisons(combinaisons: List[List[Emplacement]], sort: bool=True):
    if sort:
        combinaisons.sort(key=lambda c: get_combinaison_label(c))
    print('\n')
    for combinaison in combinaisons:
        for emplacement in combinaison:
            print(emplacement, end="")
        print("")


def get_solution():
    PLAN_PROD_SIZE = 5
    GENERATION_SIZE = 5
    MUTATION_RATE = 0.1
    bobine_store_ivoire = get_bobine_ivoire()
    all_combinaisons = get_combinaison_from_bobine_store(bobine_store_ivoire)
    generation = Generation(plan_prod_size=PLAN_PROD_SIZE,
                            generation_size=GENERATION_SIZE,
                            combinaisons=all_combinaisons,
                            mutation_rate=MUTATION_RATE)
    generation.get_individus()
    generation.sort_individu()
    print(generation)
    count_generation = 0
    while count_generation < 1:
        new_generation = generation.get_next_generation()
        print("-------NEXT GENERATION-------")
        print(new_generation)
        count_generation += 1
