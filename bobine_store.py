from typing import List, Tuple, Optional
from bobine_mere_store import BobineMere
from refente_store import Refente


class Bobine:
    def __init__(self, code: int, color: str, laize: float, longueur: int, poses: List[int]) -> None:
        self.code = code
        self.color = color
        self.laize = laize
        self.longueur = longueur
        self.poses = poses

    def __str__(self):
        return "B{}({}, {}, {}, {})".format(self.code, self.color.capitalize(), self.laize, self.longueur, self.poses)


def get_combinaison_label(combinaison: List[Tuple[Bobine, int]]) -> str:
    combinaison_as_string = ["{}-{}".format(bobine.code, pose) for (bobine, pose) in combinaison]
    combinaison_as_string = sorted(combinaison_as_string)
    return ",".join(combinaison_as_string)


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
        return list(combinaison_dic.values())

    @staticmethod
    def is_bobine_and_pose_valid_in_combinaison(combinaison: List[Tuple[Bobine, int]], bobine: Bobine, pose: int) -> bool:
        count_pose = bobine.poses.count(pose)
        count = 0
        for c_bobine_and_pose in combinaison:
            if c_bobine_and_pose == (bobine, pose):
                count += 1
        return pose == 0 or count_pose > count

    def get_combinaisons_from_refente_at_index(self, combinaison: List[Tuple[Bobine, int]], refente: Refente, index: int, condition_longueur: Optional[int]):
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
        return self.dedupe_combinaisons(new_combinaisons)

    def __str__(self):
        for bobine in self.bobines:
            print(bobine)
        return ""


bobine_store = BobineStore()
i = 0
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=130, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="prune", laize=130, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=130, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=130, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=130, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=130, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=130, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=130, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=130, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=130, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=130, longueur=700, poses=[5]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=130, longueur=700, poses=[3]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=130, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=128.5, longueur=1400, poses=[7]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=140, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=140, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=140, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=140, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="prune", laize=140, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=140, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=140, longueur=500, poses=[6]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[1]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[3]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[1]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[5]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=140, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=140, longueur=700, poses=[7]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=140, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="prune", laize=140, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ivoire", laize=140, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=140, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=140, longueur=500, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=140, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=140, longueur=500, poses=[3]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=140, longueur=500, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=140, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=140, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=140, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=140, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=140, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=140, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=140, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=140, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="prune", laize=140, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="prune", laize=140, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="prune", laize=140, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="prune", laize=140, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="prune", laize=140, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=140, longueur=500, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=140, longueur=500, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=140, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=140, longueur=500, poses=[3]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=140, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=140, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="vert", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[3]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[3]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[1]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[3]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[1]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[3]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[1]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[1]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[1]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[1]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[5]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[3]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=140, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=140, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=140, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=140, longueur=700, poses=[3]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=140, longueur=700, poses=[3]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=140, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=140, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=140, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ivoire", laize=150, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ivoire", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ivoire", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ivoire", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ivoire", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ivoire", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ivoire", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ivoire", laize=150, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ivoire", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ivoire", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ivoire", laize=150, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ivoire", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=150, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=150, longueur=500, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=150, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=150, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=150, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=150, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=150, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=150, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=150, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=150, longueur=500, poses=[3]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=150, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=150, longueur=500, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=150, longueur=500, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=150, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=150, longueur=500, poses=[3]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=150, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=150, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=150, longueur=500, poses=[1]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=150, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=150, longueur=500, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=150, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=150, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=150, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=150, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=150, longueur=500, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=150, longueur=500, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="prune", laize=150, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="prune", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="prune", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="prune", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="prune", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="prune", laize=150, longueur=500, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="prune", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="prune", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="prune", laize=150, longueur=500, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="prune", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="prune", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="prune", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="prune", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=150, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=150, longueur=500, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=150, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="vert", laize=150, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="vert", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="vert", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="vert", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="vert", laize=150, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=150, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=150, longueur=700, poses=[1]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=150, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=150, longueur=700, poses=[1]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=150, longueur=700, poses=[1, 2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=150, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=150, longueur=700, poses=[2, 2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=150, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=150, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=150, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=150, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=150, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=150, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=150, longueur=700, poses=[3]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=150, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=150, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=150, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=150, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=150, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=150, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=150, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=150, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=150, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=150, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=150, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=150, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=150, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=160, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=160, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=173.3, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=173.3, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=173.3, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=173.3, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=173.3, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=173.3, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=173.3, longueur=700, poses=[3]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=173.3, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=173.3, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=173.3, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=173.3, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=173.3, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=173.3, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ivoire", laize=180, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ivoire", laize=180, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=180, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ivoire", laize=180, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=180, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=180, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=180, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=180, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=180, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=180, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=180, longueur=500, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=180, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=180, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=180, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=180, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=180, longueur=500, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=180, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=180, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=180, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=180, longueur=500, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=180, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=180, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=180, longueur=500, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="prune", laize=180, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="prune", laize=180, longueur=500, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="prune", laize=180, longueur=500, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=180, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=180, longueur=500, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=180, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=180, longueur=500, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=180, longueur=500, poses=[3]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=180, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="vert", laize=180, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="vert", laize=180, longueur=500, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=180, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=180, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=180, longueur=700, poses=[3]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=180, longueur=700, poses=[1]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=180, longueur=700, poses=[1]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=180, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=180, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=180, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=180, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=180, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=180, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=180, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=180, longueur=700, poses=[3]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=180, longueur=700, poses=[1]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=180, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=180, longueur=700, poses=[3]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=180, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=180, longueur=700, poses=[3]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=180, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=180, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=180, longueur=700, poses=[1]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=180, longueur=700, poses=[1]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=180, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=180, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=180, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=180, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=180, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=180, longueur=700, poses=[1]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=180, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=180, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=180, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=180, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=180, longueur=700, poses=[3]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=180, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=180, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=180, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=180, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=180, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=180, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=180, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=180, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=180, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=180, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=180, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=180, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=180, longueur=700, poses=[4]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=190, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="prune", laize=190, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=190, longueur=500, poses=[1]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=190, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=190, longueur=700, poses=[1]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=190, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=190, longueur=700, poses=[1]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=190, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=190, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=190, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=190, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=190, longueur=700, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=210, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ivoire", laize=210, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=210, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="jaune", laize=210, longueur=500, poses=[1]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=210, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=210, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=210, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="prune", laize=210, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="prune", laize=210, longueur=500, poses=[1]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=210, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="vert", laize=210, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="cx", laize=210, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=210, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=210, longueur=700, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=240, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=240, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="prune", laize=240, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="cx", laize=240, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="cx", laize=240, longueur=500, poses=[1]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=260, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=260, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="noir", laize=260, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=260, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=260, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="cx", laize=260, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="cx", laize=300, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="blanc", laize=320, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="ecru", laize=320, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="marron", laize=320, longueur=500, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=320, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=320, longueur=500, poses=[2]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="orange", laize=320, longueur=500, poses=[1]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=320, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="rouge", laize=320, longueur=500, poses=[1]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="cx", laize=320, longueur=500, poses=[0]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="cx", laize=320, longueur=500, poses=[1]))
i += 1
bobine_store.add_bobine(Bobine(code=i, color="cx", laize=320, longueur=500, poses=[1]))
