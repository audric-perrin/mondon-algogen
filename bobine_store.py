from typing import List, Tuple, Optional
from bobine_mere_store import BobineMere
from refente_store import Refente

time_spent_deduping = 0


class Bobine:
    def __init__(self, code: int, color: str, laize: float, longueur: int, poses: List[int]) -> None:
        self.code = code
        self.color = color
        self.laize = laize
        self.longueur = longueur
        self.poses = poses

    def __str__(self):
        return "B{}({}, {}, {}, {})".format(self.code, self.color.capitalize(), self.laize, self.longueur, self.poses)


def get_combinaison_label(combinaison: List[Tuple[Bobine, int]]) -> int:
    combinaison_as_int = [bobine.code * (pose + 1) for (bobine, pose) in combinaison]
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
        combinaisons = self.get_combinaisons_from_refente_at_index(combinaison=[], refente=refente, index=0, condition_longueur=None)
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

    def get_bobines_and_pose_for_refente_at_index(self, refente: Refente, index: int, condition_longueur) -> List[Tuple[Bobine, int]]:
        results = []  # type : List[Tuple[Bobine, int]]
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
                        results.append((bobine, pose))
        return results

    @staticmethod
    def dedupe_combinaisons(combinaisons: List[List[Tuple[Bobine, int]]]):
        combinaison_dic = {get_combinaison_label(combinaison): combinaison for combinaison in reversed(combinaisons)}
        return combinaison_dic.values()

    @staticmethod
    def is_bobine_and_pose_valid_in_combinaison(combinaison: List[Tuple[Bobine, int]], bobine: Bobine, pose: int) -> bool:
        count_pose = bobine.poses.count(pose)
        count = 0
        for c_bobine_and_pose in combinaison:
            if c_bobine_and_pose == (bobine, pose):
                count += 1
        return pose == 0 or count_pose > count

    def get_combinaisons_from_refente_at_index(self, combinaison: List[Tuple[Bobine, int]], refente: Refente, index: int, condition_longueur: Optional[int]):
        global time_spent_deduping
        new_combinaisons = []  # type: List[List[Tuple[Bobine, int]]]
        bobines_and_poses = self.get_bobines_and_pose_for_refente_at_index(refente, index, condition_longueur)
        for bobine_and_pose in bobines_and_poses:
            bobine = bobine_and_pose[0]
            pose = bobine_and_pose[1]
            if self.is_bobine_and_pose_valid_in_combinaison(combinaison, bobine, pose):
                condition_longueur = bobine.longueur
                new_combinaison = combinaison + [(bobine, pose)]
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

    def get_time_deduping(self):
        global time_spent_deduping
        return time_spent_deduping

    def __str__(self):
        for bobine in self.bobines:
            print(bobine)
        return ""


bobine_store = BobineStore()

