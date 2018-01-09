import random
from typing import List, Tuple

from bobine_store import BobineStore, bobine_store, Bobine, get_combinaison_label
from bobine_mere_store import bobine_mere_store
from refente_store import refente_store


def get_bobine_ivoire() -> BobineStore:
    bobine_store_ivoire = BobineStore()
    for bobine in bobine_store.bobines:
        if bobine.color == "ivoire":
            bobine_store_ivoire.add_bobine(bobine)
    return bobine_store_ivoire


def display_combinaison(combinaisons: List[List[Tuple[Bobine, int]]], sort: bool=True):
    if sort:
        combinaisons.sort(key=lambda c: get_combinaison_label(c))
    for combinaison in combinaisons:
        for (bobine, pose) in combinaison:
            print("{} x {}".format(bobine, pose), end=" - ")
        print("")
    print('\n')


def get_combinaison_from_bobine_ivoire() -> List[List[Tuple[Bobine, int]]]:
    bobine_store_ivoire = get_bobine_ivoire()
    combinaisons = []
    for bobine_mere in bobine_mere_store.bobines_meres:
        refentes = refente_store.filter_for_bobine_mere(bobine_mere).refentes
        for refente in refentes:
            new_bobine_store = bobine_store_ivoire.filter_from_refente_and_bobine_mere(refente=refente,
                                                                                       bobine_mere=bobine_mere)
            new_combinaisons = new_bobine_store.get_combinaisons_from_refente(refente=refente)
            combinaisons += new_combinaisons
    dic_combinaisons = bobine_store_ivoire.dedupe_combinaisons(combinaisons)
    combinaisons = []
    for combinaison in dic_combinaisons:
        combinaisons.append(combinaison)
    return combinaisons


def get_plan_production(combinaisons: List[List[Tuple[Bobine, int]]]) -> List[Tuple[Bobine, int]]:
    plan_production = []
    count_combinaisons = len(combinaisons)
    while len(plan_production) < 10:
        plan_production.append(combinaisons[random.randint(0, count_combinaisons - 1)])
    # display_combinaison(plan_production, sort=False)
    return plan_production


class Stock:
    def __init__(self, bobine: Bobine, stock: int) -> None:
        self.bobine = bobine
        self.quantity = stock

    def __str__(self):
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

    def __str__(self):
        for stock in self.stocks:
            print(stock)
        return ""


def get_stock(plan_production: List[Tuple[Bobine, int]]) -> StockStore:
    new_stock_store = StockStore()
    for production in plan_production:
        for (bobine, quantity) in production:
            quantity = max(quantity, 1)
            new_stock_store.add_bobine(bobine, quantity)
    return new_stock_store


def get_fitness(plan_production: List[Tuple[Bobine, int]]) -> int:
    new_stock_store = get_stock(plan_production)
    fitness = 0
    for stock in new_stock_store.stocks:
        if stock.bobine.code == 403:
            fitness += stock.quantity
    return fitness


def get_first_generation(generation_size: int, combinaisons: List[List[Tuple[Bobine, int]]]) -> List[Tuple[List[Tuple[Bobine, int]], int]]:
    count_individu = 0
    generation = []
    while count_individu < generation_size:
        plan_production = get_plan_production(combinaisons)
        fitness = get_fitness(plan_production)
        generation.append((plan_production, fitness))
        count_individu += 1
    return generation
