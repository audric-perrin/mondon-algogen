from typing import List, Optional
from bobine_mere_store import BobineMere
from refente_store import Refente
from model.prod import Emplacement, Production
from model.bobine import Bobine

time_spent_deduping = 0


def get_combinaison_label(combinaison: Production) -> int:
    if not combinaison:
        return 0
    combinaison_as_int = [emplacement.bobine.code * (emplacement.pose + 1) for emplacement in combinaison.emplacements]
    combinaison_as_int = sorted(combinaison_as_int)
    count = 0
    for (index, combi_int) in enumerate(combinaison_as_int):
        count += combi_int * 1024 ** index
    return count


class BobineStore:
    def __init__(self) -> None:
        self.bobines = []  # type: List[Bobine]

    def add_bobine(self, bobine: Bobine) -> None:
        self.bobines.append(bobine)

    def filter_from_refente_and_bobine_mere(self, refente: Refente, bobine_mere: BobineMere):
        new_bobine_store = BobineStore()
        color = bobine_mere.color
        pistes = set(refente.pistes)
        for bobine in self.bobines:
            if bobine.color == color and bobine.laize in pistes:
                new_bobine_store.add_bobine(bobine)
        return new_bobine_store

    def get_combinaisons_from_refente(self, refente: Refente):
        combinaisons = self.get_combinaisons_from_refente_at_index(combinaison=Production(),
                                                                   refente=refente,
                                                                   index=0,
                                                                   condition_longueur=None)
        return combinaisons

    @staticmethod
    def get_consecutive_piste_count_at_index(refente: Refente, index: int) -> int:
        piste_laize = refente.pistes[index]
        count = 1
        for i in range(index + 1, len(refente.pistes)):
            if refente.pistes[i] == piste_laize:
                count += 1
            else:
                break
        return count

    def get_emplacement_for_refente_at_index(self,
                                             refente: Refente,
                                             index: int,
                                             condition_longueur) -> List[Emplacement]:
        results = []  # type: List[Emplacement]
        piste_count = self.get_consecutive_piste_count_at_index(refente, index)
        piste_laize = refente.pistes[index]
        for bobine in self.bobines:
            if condition_longueur:
                if bobine.longueur == condition_longueur:
                    pass
                else:
                    continue
            if bobine.laize == piste_laize:
                for pose in bobine.poses:
                    if pose <= piste_count:
                        results.append(Emplacement(bobine, pose))
        return results

    @staticmethod
    def dedupe_combinaisons(combinaisons: List[Production]):
        combinaison_dic = {get_combinaison_label(combinaison): combinaison for combinaison in reversed(combinaisons)}
        return combinaison_dic.values()

    @staticmethod
    def is_emplacement_valid_in_combinaison(combinaison: Production,
                                            emplacement_is_valid: Emplacement) -> bool:
        count = 0
        for emplacement in combinaison.emplacements:
            if emplacement.bobine == emplacement_is_valid.bobine and emplacement.pose == emplacement_is_valid.pose:
                count += 1
        return emplacement_is_valid.pose == 0 or emplacement_is_valid.pose > count

    @staticmethod
    def copy_combinaison(combinaison: Production) -> Production:
        new_combinaison = Production()
        for emplacement in combinaison.emplacements:
            new_combinaison.add_emplacement(emplacement)
        return new_combinaison

    def get_combinaisons_from_refente_at_index(self,
                                               combinaison: Production,
                                               refente: Refente,
                                               index: int,
                                               condition_longueur: Optional[int]):
        global time_spent_deduping
        new_combinaisons = []  # type: List[Production]
        emplacements = self.get_emplacement_for_refente_at_index(refente, index, condition_longueur)
        for emplacement in emplacements:
            bobine = emplacement.bobine
            pose = emplacement.pose
            if self.is_emplacement_valid_in_combinaison(combinaison, emplacement):
                condition_longueur = bobine.longueur
                new_combinaison = self.copy_combinaison(combinaison)
                new_combinaison.add_emplacement(Emplacement(bobine, pose))
                actual_pose = 1 if pose == 0 else pose
                if actual_pose + index == len(refente.pistes):
                    new_combinaisons.append(new_combinaison)
                elif actual_pose + index < len(refente.pistes):
                    next_call_combinaisons = self.get_combinaisons_from_refente_at_index(
                        combinaison=new_combinaison,
                        refente=refente,
                        index=index + actual_pose,
                        condition_longueur=condition_longueur)
                    for next_call_combinaison in next_call_combinaisons:
                        new_combinaisons.append(next_call_combinaison)
                else:
                    continue
        return new_combinaisons

    @staticmethod
    def get_time_deduping():
        global time_spent_deduping
        return time_spent_deduping

    def __str__(self):
        for bobine in self.bobines:
            print(bobine)
        return ""


bobine_store = BobineStore()
