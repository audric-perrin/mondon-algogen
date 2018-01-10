# !/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from typing import List
from model.bobine import Bobine


class Emplacement:
    def __init__(self, bobine: Bobine, pose: int):
        self.bobine = bobine
        self.pose = pose

    def __repr__(self):
        return "B{}-{} x {} -".format(self.bobine.code, self.bobine.laize, max(1, self.pose))


class Production:
    def __init__(self):
        self.emplacements = []  # type: List[Emplacement]

    def add_emplacement(self, emplacement: Emplacement):
        self.emplacements.append(emplacement)

    def __repr__(self):
        for emplacement in self.emplacements:
            print(emplacement)
        return ""


class PlanProd:
    def __init__(self, combinaisons: List[Production]):
        self.prods = []  # type: List[Production]
        self.combinaisons = combinaisons

    def get_plan_production(self, size_plan_prod: int):
        while len(self.prods) < size_plan_prod:
            alea_index_combinaison = random.randint(0, len(self.combinaisons) - 1)
            self.prods.append(self.combinaisons[alea_index_combinaison])

    def mutation(self):
        index_mutation = random.randint(0, len(self.prods) - 1)
        alea_index_combinaison = random.randint(0, len(self.combinaisons) - 1)
        self.prods[index_mutation] = self.combinaisons[alea_index_combinaison]

    def __repr__(self):
        for production in self.prods:
            print(production)
        return ""
