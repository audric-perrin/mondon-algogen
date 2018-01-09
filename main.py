import time

from refente_store import refente_store
from bobine_store import bobine_store, get_combinaison_label
from bobine_mere_store import bobine_mere_store

from bobine_data_estimate import add_all_bobines
# from bobine_data_GESCOM import add_all_bobines

add_all_bobines(bobine_store)

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


# # __________________CALCUL COMBINAISON POSSIBLE__________________
#
# bobine_results = {}
# refente_results = []
#
# t0 = time.time()
# count_combinaison = 0
# dedupe_time = 0
# bobine_count = 0
# refente_count = 0
# total_bobine = len(bobine_mere_store.bobines_meres)
# total_refente = 0
# for bobine_mere in bobine_mere_store.bobines_meres:
#     refentes = refente_store.filter_for_bobine_mere(bobine_mere).refentes
#     total_refente += len(refentes)
#
# for bobine_mere in bobine_mere_store.bobines_meres:
#     bobine_count += 1
#     bobine_mere_str = str(bobine_mere)
#     refentes = refente_store.filter_for_bobine_mere(bobine_mere).refentes
#     for refente in refentes:
#         refente_count += 1
#
#         print('\r{} bobines générées  |  {}/{} Refentes  |  {}/{} Bobines mère  |  {}  |  {}'.format(
#             str(count_combinaison),
#             refente_count,
#             total_refente,
#             bobine_count,
#             total_bobine,
#             bobine_mere,
#             refente,
#         ), end='')
#         # if bobine_mere.code == 3 and refente.code == 3:
#         #     continue
#         # if bobine_mere.code == 4 and refente.code == 0:
#         #     continue
#         # if bobine_mere.code == 4 and refente.code == 5:
#         #     continue
#         # if bobine_mere.code == 8 and refente.code == 3:
#         #     continue
#         # if bobine_mere.code == 9 and refente.code == 0:
#         #     continue
#         # if bobine_mere.code == 9 and refente.code == 5:
#         #     continue
#         # if bobine_mere.code == 9 and refente.code == 8:
#         #     continue
#         # if bobine_mere.code == 9 and refente.code == 10:
#         #     continue
#         # if bobine_mere.code == 9 and refente.code == 13:
#         #     continue
#         # if bobine_mere.code == 13 and refente.code == 0:
#         #     continue
#         t1 = time.time()
#         new_bobine_store = bobine_store.filter_from_refente_and_bobine_mere(refente=refente, bobine_mere=bobine_mere)
#         combinaisons = new_bobine_store.get_combinaisons_from_refente(refente=refente)
#         combinaisons = new_bobine_store.dedupe_combinaisons(combinaisons)
#         new_count_combinaison = len(combinaisons)
#         count_combinaison += new_count_combinaison
#         t2 = time.time()
#
#         if not bobine_results.get(bobine_mere_str):
#             bobine_results[bobine_mere_str] = ([], 0)
#         bobine_results[bobine_mere_str] = ((refente, new_count_combinaison, t2 - t1), bobine_results[bobine_mere_str][1] + t2 - t1)
#         refente_results.append((bobine_mere, refente, new_count_combinaison, t2 - t1))
#
#
# tend = time.time()
# bobine_results = bobine_results.values()
# refente_results_sorted_by_combi = sorted(refente_results, key=lambda r: r[2], reverse=True)
# refente_results_sorted_by_code = sorted(refente_results, key=lambda r: r[1].code)
# refente_results_sorted_by_code_bobine_mere = sorted(refente_results, key=lambda r: r[0].code * 10000 + r[1].code)
#
#
# def print_summary():
#     print("Temps d'exécution: {}".format(tend-t0))
#     print("Total combinaison: {}".format(count_combinaison))
#
#
# def print_refente_by_combi():
#     print('Résultat trié par combinaison')
#     print('-----------------------------')
#     for refente_result in refente_results_sorted_by_combi:
#         combi = str(refente_result[2]).rjust(6)
#         exe_time = '{:7.3f}'.format(round(refente_result[3] * 1000) / 1000)
#         bobine = str(refente_result[0]).ljust(32)
#         refente = refente_result[1]
#         print('{} -> {}s  |  {}  |  {}'.format(combi, exe_time, bobine, refente))
#
#
# def print_refente_by_code():
#     print('Résultat trié par code de refente')
#     print('---------------------------------')
#     for refente_result in refente_results_sorted_by_code:
#         combi = str(refente_result[2]).rjust(6)
#         exe_time = '{:7.3f}'.format(round(refente_result[3] * 1000) / 1000)
#         bobine = str(refente_result[0]).ljust(32)
#         refente = refente_result[1]
#         print('{} -> {}s  |  {}  |  {}'.format(combi, exe_time, bobine, refente))
#
#
# def print_refente_by_code_bobine_mere():
#     print('Résultat trié par code de bobine mère')
#     print('-------------------------------------')
#     for refente_result in refente_results_sorted_by_code_bobine_mere:
#         combi = str(refente_result[2]).rjust(6)
#         exe_time = '{:7.3f}'.format(round(refente_result[3] * 1000) / 1000)
#         bobine = str(refente_result[0]).ljust(32)
#         refente = refente_result[1]
#         print('{} -> {}s  |  {}  |  {}'.format(combi, exe_time, bobine, refente))
#
#
# print('\n')
# print_summary()
# print('\n')
# print_refente_by_combi()
# print('\n')
# print_refente_by_code()
# print('\n')
# print_refente_by_code_bobine_mere()
# print('\n')
