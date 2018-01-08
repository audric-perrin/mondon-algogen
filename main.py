from refente_store import refente_store
from bobine_store import bobine_store, get_combinaison_label
from bobine_mere_store import bobine_mere_store

# # __________________CALCUL COMBINAISON POUR UN COUPLE DE REFENTE/BOBINE MERE__________________
bobine_mere = bobine_mere_store.bobines_meres[26]
print("_____BOBINE MERE_____")
print(bobine_mere)
refente = refente_store.refentes[4]
print("_____ REFENTE_____")
print(refente)
new_bobine_store = bobine_store.filter_from_refente_and_bobine_mere(refente=refente, bobine_mere=bobine_mere)
new_count_combinaisons = new_bobine_store.get_combinaisons_from_refente(refente=refente)
new_count_combinaisons.sort(key=lambda c: get_combinaison_label(c))
for combinaison in new_count_combinaisons:
    for (bobine, pose) in combinaison:
        print("{} x {}".format(bobine, pose), end=" - ")
    print("")
print(len(new_count_combinaisons))


# __________________CALCUL COMBINAISON POSSIBLE__________________
# count_combinaison = 0
# for bobine_mere in bobine_mere_store.bobines_meres:
#     print("_____BOBINE MERE_____")
#     print(bobine_mere)
#     refentes = refente_store.filter_for_bobine_mere(bobine_mere).refentes
#     for refente in refentes:
#         print("_____LISTE REFENTE_____")
#         print(refente)
#         new_bobine_store = bobine_store.filter_from_refente_and_bobine_mere(refente=refente, bobine_mere=bobine_mere)
#         new_count_combinaison = len(new_bobine_store.get_combinaisons_from_refente(refente=refente))
#         print(new_count_combinaison)
#         count_combinaison += new_count_combinaison
# print(count_combinaison)


# # __________________CALCUL COMBINAISON BOBINE_MERE/REFENTE__________________
# i = 0
# for bobine_mere in bobine_mere_store.bobines_meres:
#     i += len(refente_store.filter_for_bobine_mere(bobine_mere).refentes)
#     print("_____BOBINE MERE_____")
#     print(bobine_mere)
#     print("_____LISTE REFENTE_____")
#     for refente in refente_store.filter_for_bobine_mere(bobine_mere).refentes:
#         print(refente)
# print("_____NOMBRE COMBINAISON_____")
# print(i)