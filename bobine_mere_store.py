from typing import List


class BobineMere:
    def __init__(self, code: int, color: str, laize: int) -> None:
        self.code = code
        self.color = color
        self.laize = laize

    def __str__(self):
        return "Bobine mère: code:{}, {} {}".format(self.code, self.color.capitalize(), self.laize)


class BobineMereStore:
    def __init__(self) -> None:
        self.bobines_meres = []  # type: List[BobineMere]

    def add_bobine(self, bobine: BobineMere) -> None:
        self.bobines_meres.append(bobine)


bobine_mere_store = BobineMereStore()
i = 0
bobine_mere_store.add_bobine(BobineMere(code=i, color='blanc', laize=560))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='blanc', laize=600))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='blanc', laize=720))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='blanc', laize=840))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='blanc', laize=980))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='cx', laize=560))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='cx', laize=720))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='cx', laize=900))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='ecru', laize=840))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='ecru', laize=980))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='ivoire', laize=600))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='ivoire', laize=720))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='jaune', laize=720))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='jaune', laize=980))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='marron', laize=600))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='marron', laize=720))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='marron', laize=840))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='noir', laize=600))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='noir', laize=720))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='noir', laize=840))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='orange', laize=560))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='orange', laize=600))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='orange', laize=720))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='orange', laize=840))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='prune', laize=720))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='prune', laize=840))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='rouge', laize=600))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='rouge', laize=720))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='rouge', laize=840))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='vert', laize=600))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='vert', laize=720))
