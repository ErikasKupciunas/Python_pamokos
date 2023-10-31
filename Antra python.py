
# # for raktas in seka:
#     print(raktas)

# for i in range(5):
#     print("skaicius", i)

# sarasas = [1,2,3,4,5,6]
# for skaicius in skaiciai:
#     print("mano saraso skaicius", skaicius)
#
# tekstas = "pyhon data science"
# for raide in tekstas:
#     print(raide)

# zodynas = {"a":1, "b":2, "c":3}
#
# # for raktas in zodynas:
# #     print(raktas, zodynas[raktas])
# #
#

# sarasas = [1,2,3,4,5]
# for skaicius in sarasas:
#     if skaicius == 3:
#         break
#     print(skaicius)    sustoja ties skaiciu trys

# sarasas = [1,2,3,4,5]
# for skaicius in sarasas:
#     if skaicius == 3:
#         continue
#     print(skaicius)  randa visus skaicius iskyrus trejeta


# rasti skaicius kurie yra daugiau uz visu skaiciu vidurki

# skaiciai = [10,20,30,40,50]
#
# suma = sum(skaiciai)
#
# vidurkis = suma /len(skaiciai)
# # print("gautas vidurkis" vidurkis)
#
# for skaicius in skaiciai:
#     if skaicius > vidurkis:
#         print(skaicius)

#
# sarasas = ["jonas","antanas", "ona","marija"]
# print('\n'.join(sarasas)
# # for vardas in sarasas:
# #     print(vardas+'\n')

# Parasyt python atvirksciai su for

# tekstas_1 = "python"
# tekstas_2 = ""
# for raide in tekstas_1:
#     tekstas_2 = raide+tekstas_2
#     print(tekstas_2)

# Atspausdinti visa daugybos lentele

# daugybos_lentele  = 10
# for i in range(1,daugybos_lentele + 1):
#     for j in range(1,daugybos_lentele +1):
#         print(i*j, end='\t')
#     print()

# # PARASYTI SAKINI IS ZODZIU SARASO BE KABUCIU IR KABLELIU
# sarasas = ["labas", "rytas", "pasauli"]
# sarasas2 = ""
# for zodis in sarasas:
#     sarasas2 += zodis +" "
# print(sarasas2)

# sarasas = ["labas", "rytas", "suraitytas", "skanios", "kavytes"]
# for i in sarasas:
#     print(i, end="_")   #paprastesnis variantas


# WHILE

# skaicius = 1
# while skaicius <= 20:
#     print(skaicius)
#     skaicius += 1

# ivestis = int(input("iveskite teigiama skaiciu_>"))
#
# while ivestis < 0:
#     print("jusu skaicius neigiamas")
#     ivestis = int(input("Banddykite dar karta_>"))
# print("iveskite teigiama skaicius")


# ZAIDIMAS ATSPETI SKAICIU
# atsakymas = 5
# spejimas = int(input("spekite skaiciu nuo 1 iki 10:"))
#
# while spejimas != atsakymas:
#     spejimas = int(input("Neteisingas atsakymas! Bandykite dar karta:"))
#
# print("Sveikiname Atspejote")


# while True:
#     print("-------Menu------")
#     print("1.Atspausdinti pasisveikinima")
#     print("2. Iveskite nauja varda")
#     print("3 Iseiti")
#
#     pasirinkimas = input("Iveskite savo pasirinkima (1/2/3):")
#     if pasirinkimas == "1":
#         print(f"labas")
#     elif pasirinkimas == "2":
#         vardas = input("iveskite nauja varda:")
#
#         print("Sekmingai ivedete nauja varda!")
#         print (f"Jusu vardas pakeistas i {vardas}")
#     elif pasirinkimas == "3":
#         print("Aciu kad naudojates programa. IKI")
#         break
#     else:
#         print("Neteisingas pasirinkimas! Bandykite dar karta")


          #PARASYTI PROGRAMA KURIOJE NURODYTAS PASLAPTINGAS ZODIS

# paslaptingas_zodis = "langas"
# spejimas = input("Spekite paslaptinga zodi")
#
# while spejimas != paslaptingas zodis:
#     spejimas = input("spekite paslaptinga zodi")
#     print("Sveikiname atspejote")


# max_skaicius = 11
# pasirinkimas = int(input("pasirinkite skaiciu nuo 1 iki 10"))
# while max_skaicius <=10:
#     rezultatas = max_skaicius*pasirinkimas
#     print(f'{pasirinkimas} *{max_skaicius} = {rezultatas}')
#     max_skaicius += 1



# FUNKCIJOS
# Sintakse funkcijose: def funkcijospavadinimas (argumentai)

# def pasisveikinti(vardas):
#     print(f"hello {vardas}")
#
# pasisveikinti("Erikas")
#
# if __name__ == '__main__':
#     pasisveikinti ()


# def suma (a,b):
#     return a + b
# atsakymas = suma(5,3)
# print (atsakymas)
#
# if __name__=='__main__':
#     suma (5,3)
#
# def rodyti_meniu():
#     print("----Meniu----")
#     print("1.Perziureti viskas knygas")
#     print("2.ieskoti knygos pagal pavadinima")
#     print("3.Iseiti")
#
# def prideti_knyga (knygu_sarasas):
#     pavadinimas = input("Iveskite knygos pavadinima")
#     autorius = input("iveskite knygos autoriu:")
#     knygu_sarasas.append({"pavadinimas": pavadinimas, "autorius":autorius})
#     print(f"Knyga '{pavadinimas}' prideta!")
#
# def perziureti_knygas(knygu_sarasas):
#     for knyga in knygu_sarasas:
#         print(f"Pavadinimas: {knyga['pavadinimas']}, Autorius: {knyga['autorius']}")
#
# def ieskoti_knygos (knygu_sarasas):
#     ieskomas_pavadinimas = input("iveskite knygos pavadinima kurios ieskote:")
#     rasti_knygas = [knyga for knyga in knygu_sarasas if ieskomas_pavadinimas.lower() in knyga["pavadinimas"].lower()]
#
#     if rasti_knygas:
#         for knyga in rasti_knygas:
#             print(f"Pavadinimas: {knyga['pavadinimas']}, autorius: {knyga['autorius']}")
#         else:
#             print(f" knyga su pavadinimu: '{ieskomas_pavadinimas}' nerasta")
#
#
# def main ():
#     knygu_sarasas = []
#
#     while True:
#         rodyti_meniu()
#         pasirinkimas = input("pasirinkite veiksma (1-4)")
#         if pasirinkimas == "1":
#             prideti_knyga(knygu_sarasas)
#         elif pasirinkimas == "2":
#             perziureti_knygas(knygu_sarasas)
#         elif pasirinkimas == "3":
#             perziureti_knygas(knygu_sarasas)
#         elif pasirinkimas == "4":
#             perziureti_knygas(knygu_sarasas)
#             print(Geros_dienos)
#             break
#         else:
#             print("Neteisingas_pasirinkimas")
#
# if __name__=='__main__'

# def rodyti_meniu():
#     print("-----Meniu-----")
#     print("1. Prideti knyga")
#     print("2. Perziureti visas knygas")
#     print("3. Ieskoti knygos pagal pavadinima")
#     print("4. Iseiti")

#
# def prideti_knyga(knygu_sarasas):
#     pavadinimas = input("Iveskite knygos pavadinima_>")
#     autorius = input("Iveskite knygos autoriu_>")
#     knygu_sarasas.append({"pavadinimas": pavadinimas,"autorius":autorius})
#     print(f"Knyga '{pavadinimas}' prideta!")
#
# def perziureti_knygas(knygu_sarasas):
#     for knyga in knygu_sarasas:
#         print(f"Pavadinimas: {knyga['pavadinimas']}, Autorius: {knyga['autorius']}")
#
#
# def ieskoti_knygos(knygu_sarasas):
#     ieskomas_pavadinimas = input("Iveskite knygos pavadinima kurios ieskote_>")
#     rasti_knygas = [knyga for knyga in knygu_sarasas if ieskomas_pavadinimas.lower() in knyga['pavadinimas'].lower()]
#
#     if rasti_knygas:
#         for knyga in rasti_knygas:
#             print(f"Pavadinimas: {knyga['pavadinimas']}, Autorius: {knyga['autorius']}")
#     else:
#         print(f" Knyga su pavadinimu: '{ieskomas_pavadinimas}' nerasta")
#
#
# def main():
#     knygu_sarasas = []
#
#     while True:
#         rodyti_meniu()
#         pasirinkimas = input("Pasirinkite veiksma(1-4)_>")
#         if pasirinkimas == "1":
#             prideti_knyga(knygu_sarasas)
#         elif pasirinkimas == "2":
#             perziureti_knygas(knygu_sarasas)
#         elif pasirinkimas == "3":
#             ieskoti_knygos(knygu_sarasas)
#         elif pasirinkimas == "4":
#             print("Iki greito!")
#             break
#         else:
#             print("Neteisingas pasirinkimas. Prasome pasirinkti nuo 1 iki 4")
#
# if __name__ == '__main__':
#     main()
#
#

#Bankine sistema
# banko_saskaitos = {
#
# }
#
# def rodyti_meniu():
#     print("-----Banko sistema-----")
#     print("1. Atidaryti gauta saskaita")
#     print("2. inesti pinigus")
#     print("3. isimti pinigus")
#     print("4. perziureti saskaitos likuti")
#     print("5. uzdaryti saskaita")
#     print("6. iseiti")
#
# def prideti_saskaita(paslaugos):
#     saskaitos_turetojas = input("Iveskite varda: ")
#     pradinis_likutis = int(input("Iveskite pradini likuti: "))
#     saskaitos_nr = len(banko_saskaitos) + 1
#     Banko_saskaitos[saskaitos_nr] = { "saskaitos_turetojas": saskaitos_turetojas, "pradinis_likutis": pradinis_likutis}
#     print(f"Nauja saskaita '{saskaitos_numeris}' prideta")
#
#
# def inesti_pinigus(paslaugos)
# suma = int(input("idekite pinigu suma: "))
# saskaitos_nr int(input("Iveskite saskaitos nr:"))
# banko_saskaitos [saskaitos_nr]["pradinis_likutis!"] += suma
# print(F" I saskaita nr.:{saskaitos_nr}'sekmingai inesta '{suma}'")
#
# def nusiimti pinigus(paslaugos)
# suma = int(input("idekite nuimamu pinigu suma: "))
# saskaitos_nr int(input("Iveskite saskaitos nr:"))
# banko_saskaitos [saskaitos_nr]["pradinis_likutis!"] -= suma
#     if suma <= banko_saskaitos[saskaitos_nr]["pradinis_likutis"]:
#         banko_saskaitos[saskaitos_nr]["pradinis_likutis"] -= suma
#         print(f" Is saskaitos nr.:{saskaitos_nr}'sekmingai isimta '{suma}'")
#     else
#         print(f"Jusu pradinis likutis yra per mazas. Jis yra:'{banko_saskaitos[saskaitos_nr]['pradinis likutis']} eurai")
#
# def perziureti_likuti(paslaugos):
#     saskaitos_nr = int(input("Iveskite saskaitos nr"))
#     likutis = banko_saskaitos[saskaitos_nr]["pradinis_likutis"]
#     print(f'Saskaitos nr.:'{saskaitos_nr}', likutis yra: '{likutis}' eurai")
# def istrinti_saskaita(paslaugos)
#     saskaitos_nr = int(input("Iveskite saskaitos nr.:"))
#     del banko_saskaitos[saskaitos_nr]
#     print(f"banko sask {saskaitos_nr} buvo istrina")
#
# def main ():
#     while True
#         rodyti meniu()
#         pasirinkimas = input("pasirinkite veiksma")
#         if pasirinkimas == "1":
#             prideti_saskaita(banko_saskaitos)
#         elif pasirinkimas == "2":
#             inesti_pinigus(banko_saskaitos)
#         elif pasirinkimas == "3":
#             nusiimti_pinigus(banko_saskaitos)
#         elif pasirinkimas == "4":
#             perziureti_likuti(banko_saskaitos)
#         elif pasirinkimas == "5":
#             istrinti_saskaita(banko_saskaitos)
#         elifpasirinkimas == "6":
#             print("Viso gero")


#bankine sistema. mes galime atidaryti sas, inesti pin, nusiimti pin, perziureti liktui, uzdaryti sas, iseiti is sistemos:

# def pvm_skaiciuokle(kaina):
#     pvm_tarifas = 0.21
#     kaina_su_pvm = kaina + kaina * pvm_tarifas
#     print(kaina_su_pvm, "kaina su pvm")
#     pvm_skaiciuokle(10)
#

# def pvm_skaiciuokle(kaina):
#     pvm_tarifas = 0.21
#     kaina_su_pvm = kaina + kaina * pvm_tarifas
#     print(kaina_su_pvm, 'kaina su PVM.')
#
#
# kaina_be_pvm = int(input("Kaina be PVM:"))
# pvm_skaiciuokle(kaina_be_pvm)

