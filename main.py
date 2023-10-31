
# vardas = "Jonas" # String
# amzius = "30" #int
# ar_jonas_moka_programuot = False  #bool
# jono_pirkiniu_suma = 34.5 #float
# print("Mano draugo vardas yra " + vardas + "Jo amzius ",  amzius, ar_jonas_moka_programuot,jono_pirkiniu_suma)

# print(type(amzius)) # kokio tipo parodo (Str, int ir t.t.)


# #listas(array) masyvas = []
# vaisiai = ["Obuolys",'Arbuzas','Bananas','Kriause']
# # ilgis = len(vaisiai)
# # # pridedame_vaisiu = vaisiai.append("Melionas")
# # vaisiai.insert(1,"Melionas") // idedamas naujas vaisius
# # vaisiai[1] = "Kivis" keiti reiksme liste
# # indexas = vaisiai.index("Arbuzas") //parodo kur yra arbuzas (jo indexas)
# # vaisiai.remove("Bananas") //istraukia is saraso Banana
# # vaisiai.pop(2) //istraukia pagal indexa (isemus pasikeicia indexacija)
# print(vaisiai[1])

# Zodynas

# dictionary - structure = my_dict = (key1:value1, key2:value2)
# zodynas = {
#     "Vardas": "Jonas",
#     "Amzius": 30,
#     "Miestas": "Vilnius"
# }
# # zodynas ["ar_studentas"] = True
# # del zodynas["Miestas"] Istrinti
# print(zodynas)
#
#
# studentai = [
#     {
#     "Vardas": "Jonas",
#     "Amzius": 32,
#     "Miestas": "Kaunas",
#     "Profesija": "Inzinierius"
#     },
#     {
#     "Vardas": "Ona",
#     "Amzius": 25,
#     "Miestas": "Klaipeda",
#     "Profesija": "Gyditoja"
# },
# Naujas studentas = {
#     "Vardas": "Antanas",
#     "Amzius": 46,
#     "Miestas": "Vilnius",
#     "Profesija": "Mokytojas"
# }]
#
# studentai.append(naujas_studentas)
# print(studentai) GRYZTI CIA

# IF SALYGA
#
# # if salyga if salyga: jusu veiksmai

# amzius = 17
# if amzius >= 18:
#     print("Asmuo yra pilnametis")
# elif amzius > 13:
#     print("Asmuo yra paauglys")
# else:
#     print("Asmuo nera pilnametis")
#
# vaisiai = ["kivis"]
#
# if not vaisiai:
#     print("vaisiu sarasas tuscias")
# elif "kivis" in vaisiai:
#     print("vaisius kivis")
# else:
#     print("vaisius kivis nerastas, taciau sarase yra elementu")

# age = 18
# has_id = true
# If age >= 18:
#     if has_id
#         print("gali balsuoti")
#     else:
#         print("jusms reikia asmens tapatybes koreles")
#     else:
#     print("jums dar negalima balsuoti")

# REALUS PAVYZDYS 11:24 LAIKU
#
# prekiu_kategorijos = ["Vaisiai", "mesa", "darzoves"]
#
# prekes = {
#     "vaisiai": ['Obuoliai', 'Bananu'],
#     "mesa": ['kiauliena', 'Vistiena'],
#     "darzoves": ['Bulves', 'Pomidorai']
# }
# # Norime rasti prees kategorija "mesa" ir prekes Vistiena
#
# norima_kategorija = "Mesa"
# norima_preke = "Vistiena"
#
# if norima_kategorija in prekiu_kategorijos:
#     if norima_preke in prekes [norima_kategorija]:
#         print(f"parduotuveje yra '{norima_preke}'")
#     else:
#         print(f"Parduotuveje nera '{norima_preke}'")
# else:
#         print("Parduotuveje nera prekiu kategorijos: {norima_kategorija}")


#
# zmones = [
#     {"Vardas": "Tomas",
#     "Amzius": 23},
#
#     {"Vardas": "Rita",
#     "Amzius": 26},
#
#     {"Vardas": "Jonas",
#     "Amzius": 30},
#
#     {"Vardas": "Petras",
#     "Amzius": 55},
#
#     {"Vardas": "Tadas",
#     "Amzius": 17}
# ]
#
# zmogus = zmones[0]
# if zmogus ["Amzius"] > 18:
#     print(f' sis zmogus {zmogus["Vardas"]} yra suauges')
#     if zmogus ["Amzius"] == 18:
#         print(f' sis zmogus {zmogus["Vardas"]} paauglys')
#         if zmogus["Amzius"] < 18:
#             print(f' sis zmogus {zmogus["Vardas"]} nepilnametis')


# Darbuotojas = {
#     "Vardas": "Tomas",
#     "Atlyginimas": 2200,
#     "Pareigos": "siuvejas"
# }
# if Darbuotojas["Pareigos"] == "inzinierius":
#     Darbuotojas['Atlyginimas'] = Darbuotojas ['Atlyginimas'] * 1.10
#     # trumpesnis variantas
#     # print(Atlyginimas) *= 1.10

# knygos =[
#     {"pavadinimas": "Haris Poteris", "isleidimo_metai": 1997},
#     {"pavadinimas": "Moby Dick", "isleidimo_metai": 1812},
#     {"pavadinimas": "Metai", "isleidimo_metai": 1997},
# ]
#
# # Knyga_pagal_ieskomus_metus = int(input("iveskite knygos isleidimo metus_>"))
# # knyga = knygos
# #
# # if knyga[0]["isleidimo_metai"] == knyga_pagal_ieskomus_metus:
# #     print(f"knyga isleista {Knyga_pagal_ieskomus_metus}) metais yra: {knyga[0]['pavadinimas']}")
# # else:
# #     print("tokia knyga nerasta")
#
#
#
# knygos =[
#     {"pavadinimas": "Haris Poteris", "isleidimo_metai": 1997},
#     {"pavadinimas": "Moby Dick", "isleidimo_metai": 1812},
#     {"pavadinimas": "Metai", "isleidimo_metai": 1997},
# ]
# knyga_pagal_ieskomus_metus = int(input("Iveskite knygos isleidimo metus kuriu ieskote_> "))
#
# if knygos[0]["isleidimo_metai"] == knyga_pagal_ieskomus_metus:
#     print(f"knyga isleista {knyga_pagal_ieskomus_metus} metais yra: {knygos[0]['pavadinimas']}")
# elif knygos[1]["isleidimo_metai"] == knyga_pagal_ieskomus_metus:
#     print(f"Knyga, išleista {knyga_pagal_ieskomus_metus} metais, yra: {knygos[1]['pavadinimas']}.")
# elif knygos[2]["isleidimo_metai"] == knyga_pagal_ieskomus_metus:
#     print(f"Knyga, išleista {knyga_pagal_ieskomus_metus} metais, yra: {knygos[2]['pavadinimas']}.")
# else:
#     print(f"Deja, knygų_išleistų {knyga_pagal_ieskomus_metus} metais nėra.")
#

#
# IMPORTUOJAMOS BIBLIOTEKOS VISADA RASOMA PIRMOSE EILUTESE
import os
