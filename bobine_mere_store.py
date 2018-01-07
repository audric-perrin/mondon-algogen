from typing import List


class BobineMere:
    def __init__(self, code: int, color: str, largeur: int) -> None:
        self.code = code
        self.color = color
        self.largeur = largeur


class BobineMereStore:
    def __init__(self) -> None:
        self.bobines_meres = []  # type: List[BobineMere]

    def add_bobine(self, bobine: BobineMere) -> None:
        self.bobines_meres.append(bobine)


bobine_mere_store = BobineMereStore()
i = 0
bobine_mere_store.add_bobine(BobineMere(code=i, color='blanc', largeur=560))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='blanc', largeur=600))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='blanc', largeur=720))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='blanc', largeur=840))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='blanc', largeur=980))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='cx', largeur=560))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='cx', largeur=720))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='cx', largeur=900))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='ecru', largeur=840))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='ecru', largeur=980))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='ivoire', largeur=600))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='ivoire', largeur=720))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='jaune', largeur=720))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='jaune', largeur=980))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='marron', largeur=600))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='marron', largeur=720))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='marron', largeur=840))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='noir', largeur=600))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='noir', largeur=720))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='noir', largeur=840))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='orange', largeur=560))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='orange', largeur=600))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='orange', largeur=720))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='orange', largeur=840))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='prune', largeur=720))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='prune', largeur=840))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='rouge', largeur=600))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='rouge', largeur=720))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='rouge', largeur=840))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='vert', largeur=600))
i += 1
bobine_mere_store.add_bobine(BobineMere(code=i, color='vert', largeur=720))
