import os
#
# dabartinis_katalogas = os.getcwd()
# print(dabartinis_katalogas)
# norimas_aplankas = input("iveskite aplanko pavadinima, kurio turini norite matyti: ")
# naujas_katalogas = input("praso, nurodyti katalogo lokacija:")
# keiciam_kataloga = os.chdir(naujas_katalogas)
#
# try:
#     keiciam_kataloga = os.chdir(naujas_katalogas)
#     if os.getcwd() == naujas_katalogas:
#         print(f"Darbinis katalogas sekmingai pakeistas i {naujas_katalogas}")
#     turinys = os.listdir(norimas_katalogas)
#     print (dabartinis_katalogas)
#     print(", ".join(turinys))
# except FileNotFoundError:
#     print(f"Deja aplankas '{naujas_katalogas})' nerastas")

# import shutil
#
# EXTENSION_MAP ={
#     ".jpg": "Images",
#     ".pdf": "Documents",
#     ".jpeg": "Images",
#     ".txt": "Text"
# }
# filename = input("please set the name you want to organize_>")
#
# File_extension = os.path.splitext(filename)[1]
#
# try:
#     if os.path.exists(filename) and File_extension in EXTENSION_MAP:
#         directory_name = EXTENSION_MAP[File_extension]
#         # create the dictionary
#         if not os.path.exists(directory_name):
#             os.makedirs(directory_name)
#
# # move the file
#         shutil.move(filename, os.path.join(directory_name, filename))
#         print(f"{filename} has been moved to {directory_name}")
#     else:
#         print("the file does not exist or its extension is not recognized")
# except FileNotFoundError:
#     print(f"Error: {filename} was not found")
# except PermissionError:
#     print(f"Error: You dont have permision to move '{filename}'")



# # Antras:
# #
# zodynas = {
#     {"Vardas": "Tomas",
#     "egzamino_rezultatas": 9},
#
#     {"Vardas": "Rita",
#     "egzamino_rezultatas": 10},
#
#     {"Vardas": "Jonas",
#     "egzamino_rezultatas": 6},
#
#     {"Vardas": "Petras",
#     "egzamino_rezultatas": 5},
#
#     {"Vardas": "Tadas",
#     "egzamino_rezultatas": 3}
# }
# Studentas = zodynas[2]
# if studentas ["egzamino_rezultatas"] >= 5:
#     print(f' sis studentas {studentas["Vardas"]} egzamina islaike')
#     if studentas ["egzamino_rezultatas"] >5:
#         print(f' sis studentas {studentas["Vardas"]} egzamino neislaike')
#
#
#
# # # Pirmas
# #
# prekiu_sarasas = ["preke","kaina"]
#
# prekes = [
#
#     {"preke": "Obuolys",
#     "kaina": 2 },
#
#     {"preke": "Batonas",
#     "kaina": 1.50 },
#
#     {"preke": "Arbuzas",
#     "Kaina": 2.50 },
#
#     {"preke": "kriause",
#     "Kaina": 5 }
# ]
#

class Uzduotis:

    def __init__(self, pavadinimas, aprasymas):
        self.pavadinimas=pavadinimas
        self.aprasymas=aprasymas
        self.atlikta=False

    def atlikimas(self):
        self.atlikimas=True
        print (f"Uzduotis {self.pavadinimas} buvo atlikta ")

    def info(self):
        return f"Pavadinimas {self.pavadinimas}\n  Aprasymas: {self.aprasymas}\n  "


class ToDo_sarasas:
    def __init__(self):
        self.uzduociu_sarasas=[]

    def prideti_uzduoti(self, pavadinimas, aprasymas):
        uzduotis = Uzduotis(pavadinimas,aprasymas)
        self.uzduociu_sarasas.append(uzduotis)

    def visos_uzduotys(self):
        if not self.uzduociu_sarasas:
            print("Uzduociu sarasas yra tuscias")
        for uzduotis in self.uzduociu_sarasas:
            print(uzduotis.info())

    def pazymeti_kaip_atlikta(self,pavadinimas):
        for uzduotis in self.uzduociu_sarasas:
            if uzduotis.pavadinimas==pavadinimas:
                uzduotis.atlikimas()
                return
        print (f' uzduotis pavadinimu: {pavadinimas} nerasta')


ToDo_sarasas=ToDo_sarasas()
while True:
    print("\n Pasirinkite veiksma:")
    print("1. prideti uzduoti")
    print("2. Perziureti uzduoti")
    print("3. Pazymeti uzduoti kaip atlikta")
    print ("4. Iseiti")

    pasirinkimas= input()
    if pasirinkimas=="1":
        pavadinimas= input("Iveskite uzduoties pavadinima---->")
        aprasymas=input("Iveskite uzduoties aprasyma---->")
        ToDo_sarasas.prideti_uzduoti(pavadinimas,aprasymas)
        print("Uzduotis sekmingai prideta")
    elif pasirinkimas=="2":
        ToDo_sarasas.visos_uzduotys()
    elif pasirinkimas=="3":
        pavadinimas= input("Iveskite uzduoties pavadinima kuria norite pakeisti --->")
        ToDo_sarasas.pazymeti_kaip_atlikta(pavadinimas)
    elif pasirinkimas=="4":
        print("Iseinama....")
        break
    else:
        print("neteisingas pasirinkimas prasome bandyti dar karta ")