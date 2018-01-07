from typing import List


class Refente:
    def __init__(self, code: int, pistes: List[float]) -> None:
        self.pistes = pistes
        self.laizes = round(sum(self.pistes))


class RefenteStore:
    def __init__(self) -> None:
        self.refentes = []  # type: List[Refente]

    def add_refente(self, refente: Refente) -> None:
        self.refentes.append(refente)


refente_store = RefenteStore()
i = 0
refente_store.add_refente(Refente(code=i, pistes=[140, 140, 140, 140, 140, 140, 140]))
i += 1
refente_store.add_refente(Refente(code=i, pistes=[180, 140, 140, 140]))
i += 1
refente_store.add_refente(Refente(code=i, pistes=[150, 140, 140, 140, 150]))
i += 1
refente_store.add_refente(Refente(code=i, pistes=[140, 140, 140, 140, 140, 140]))
i += 1
refente_store.add_refente(Refente(code=i, pistes=[140, 140, 140, 140]))
i += 1
refente_store.add_refente(Refente(code=i, pistes=[130, 150, 140, 140, 140, 140, 140]))
i += 1
refente_store.add_refente(Refente(code=i, pistes=[150, 150, 150, 150]))
i += 1
refente_store.add_refente(Refente(code=i, pistes=[320, 260, 140]))
i += 1
refente_store.add_refente(Refente(code=i, pistes=[130, 180, 180, 180, 180, 130]))
i += 1
refente_store.add_refente(Refente(code=i, pistes=[180, 180, 180, 180]))
i += 1
refente_store.add_refente(Refente(code=i, pistes=[140, 173.3, 173.3, 173.3, 180, 140]))
i += 1
refente_store.add_refente(Refente(code=i, pistes=[160, 150, 180, 180, 150, 160]))
i += 1
refente_store.add_refente(Refente(code=i, pistes=[210, 150, 150, 210]))
i += 1
refente_store.add_refente(Refente(code=i, pistes=[140, 140, 173.3, 173.3, 173.3, 180]))
i += 1
refente_store.add_refente(Refente(code=i, pistes=[190, 150, 150, 150, 150, 190]))
i += 1
refente_store.add_refente(Refente(code=i, pistes=[150, 150, 150, 150]))
i += 1
refente_store.add_refente(Refente(code=i, pistes=[180, 160, 150, 150, 160, 180]))
i += 1
refente_store.add_refente(Refente(code=i, pistes=[128.5, 128.5, 128.5, 128.5, 128.5, 128.5, 128.5]))
i += 1
refente_store.add_refente(Refente(code=i, pistes=[260, 260, 320]))
i += 1
refente_store.add_refente(Refente(code=i, pistes=[240, 240, 240]))
i += 1
refente_store.add_refente(Refente(code=i, pistes=[320, 240]))
i += 1
refente_store.add_refente(Refente(code=i, pistes=[260, 260, 320]))
i += 1
refente_store.add_refente(Refente(code=i, pistes=[210, 210, 210, 210]))
i += 1
