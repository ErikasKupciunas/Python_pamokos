# OBJEKTINIS PROG:
#
# class Automobilis:
#     def __init__(self,marke, modelis, metai, variklio_turis, kuro_tipas, rida):
#         self.marke = marke
#         self.modelis = modelis
#         self.metai = metai
#         self.variklio_turis = variklio_turis
#         self.kuro_tipas = kuro_tipas
#         self.rida = 0
#
#     def automobilio_pavadinimas(self):
#         return f"Automobilis: {self.marke}\nAutomobilio_modelis:{self.modelis}\nPagaminimo_metai{self.metai}\n"
#
#
#     def vaziuoti(self, km):
#             self.rida =+ km
#             return f"Vaziuojama {km}km, Bendra rida {self.rida}km"
#
# Auto1 = Automobilis("Audi","A8",2021,variklio_turis, kuro_tipas)
#
# print(Auto1.automobilio_pavadinimas())
# print(Auto1.automobilio_pavadinimas())
# print(Auto1.vaziuoti (150))















# class Gyvunas(object):
#     def __init__(self,rusis, svoris, amzius, vardas):
#         self.rusis = rusis
#         self.amzius = amzius
#         self.svoris = svoris
#         self.vardas = vardas
#
#     def Gyvuno_apibudinimas(self):
#         return f"Gyvuno rusis: {self.rusis}\n Jo svoris {self.svoris,}\n Jo amzius {self.amzius}\n Vardas: {self.vardas}"
#
#     def valgo(self):
#         return f"{self.vardas} eina valgyti"
#
#     def prisistatymas(self):
#         return f" As esu {self.rusis} ir mano vardas yra {self.vardas}"
#
# kate = Gyvunas("siamo", 10, 12, "Kacius")
#
# print(kate.Gyvuno_apibudinimas())
# print(kate.valgo())
# print(kate.prisistatymas())


















#NAUJAS 10;28 LAIKAS RENATOS IDETAS KODAS


# class Uzduotis:
#
#     def __init__(self, pavadinimas, aprasymas):
#         self.pavadinimas=pavadinimas
#         self.aprasymas=aprasymas
#         self.atlikta=False
#
#     def atlikimas(self):
#         self.atlikimas=True
#         print (f"Uzduotis {self.pavadinimas} buvo atlikta ")
#
#     def info(self):
#         return f"Pavadinimas {self.pavadinimas}\n  Aprasymas: {self.aprasymas}\n  "
#
#
# class ToDo_sarasas:
#     def __init__(self):
#         self.uzduociu_sarasas=[]
#
#     def prideti_uzduoti(self, pavadinimas, aprasymas):
#         uzduotis = Uzduotis(pavadinimas,aprasymas)
#         self.uzduociu_sarasas.append(uzduotis)
#
#     def visos_uzduotys(self):
#         if not self.uzduociu_sarasas:
#             print("Uzduociu sarasas yra tuscias")
#         for uzduotis in self.uzduociu_sarasas:
#             print(uzduotis.info())
#
#     def pazymeti_kaip_atlikta(self,pavadinimas):
#         for uzduotis in self.uzduociu_sarasas:
#             if uzduotis.pavadinimas==pavadinimas:
#                 uzduotis.atlikimas()
#                 return
#         print (f' uzduotis pavadinimu: {pavadinimas} nerasta')
#
#
# ToDo_sarasas=ToDo_sarasas()
# while True:
#     print("\n Pasirinkite veiksma:")
#     print("1. prideti uzduoti")
#     print("2. Perziureti uzduoti")
#     print("3. Pazymeti uzduoti kaip atlikta")
#     print ("4. Iseiti")
#
#     pasirinkimas= input()
#     if pasirinkimas=="1":
#         pavadinimas= input("Iveskite uzduoties pavadinima---->")
#         aprasymas=input("Iveskite uzduoties aprasyma---->")
#         ToDo_sarasas.prideti_uzduoti(pavadinimas,aprasymas)
#         print("Uzduotis sekmingai prideta")
#     elif pasirinkimas=="2":
#         ToDo_sarasas.visos_uzduotys()
#     elif pasirinkimas=="3":
#         pavadinimas= input("Iveskite uzduoties pavadinima kuria norite pakeisti --->")
#         ToDo_sarasas.pazymeti_kaip_atlikta(pavadinimas)
#     elif pasirinkimas=="4":
#         print("Iseinama....")
#         break
#     else:
#         print("neteisingas pasirinkimas prasome bandyti dar karta ")













# KITA UZDUOTIS 12:47. sukurti saskaita

# class saskaita:
#     def __init__(self, vardas, pavarde,pradinis_likutis=0):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.pradinis_likutis = pradinis_likutis=0
#
#     def Inesti_pinigu(self, suma):
#         if suma > 0:
#             self.pradinis_likutis += suma
#         else:
#             print("Klaida, negalima ideti neigiamos sumos")
#     def nusiimti_pinigu(self, suma):
#         if suma > 0:
#             if suma < self.pradinis_likutis:
#                 self.pradinis_likutis -= suma
#                 print(f"Jus sekmingai nusiemete {suma}")
#             else:
#             print("klaida, jusu likutis nepakankamas")
#         else:
#         print("Negalima nusiimti neigiamos sumos")
#
#
#     def saskaitos_likutis(self):
#         return f"Kliento {self.vardas} {self.pavarde} saskaitos likutis yra {self.pradinis_likutis}"
#
# numeris_vienas = saskaita("Jonas", "Jonaitis")
# print(numeris_vienas.saskaitos_likutis())
#
# numeris_vienas.inesti_pinigu(400)
# numeris_vienas.nusiimti_pinigu(-200)
# print(numeris_vienas.saskaitos_likutis())



# Sukurkite Studentas klase kuri reprezentuoja individualų studentą, turintį savo vardą, pavardę, amžių, studento
# numerį ir pažymių sąrašą. Antroje klasėje StudentuValdymoSistema - tai klasė, skirta valdyti studentų
# sąrašą. Ji leidžia pridėti naujus studentus, gauti informaciją apie konkretų studentą pagal jo numerį ir išvesti visų studentų informaciją.

class Studentai:
    def __init__(self, vardas, pavarde, amzius, studento_numeris, pazymiai=None):
        self.vardas = vardas
        self.pavarde = pavarde
        self.amzius = amzius
        self.Studento_numeris = Studento_numeris
        self.Pazymiai = Pazymiai if pazymiai else []

    def pasalinti.prideti_pazymi()mi(self.pazymys)
        if 0 <= pazymys < len(self.pazymiai):
            del self.pazymiai
        else:
            print("toks pazymys nerastas")

    def studento_vidurkis(self)
        return sum(self.pazymiai) / len(self.pazymiai) if self.pazymiai else 0

    def prideti_pazymi(self,pazimys):
        self.pazymiai.append(pazimys)

class StudentuValdymoSistema:
    def __init__(self):
        self.studentu_sarasas = []

    def prideti_studenta(self, studentas)
        self.studentu_sarasas.append(studentas)
        print("Studentas sekmingai pridetas")

    def pasalinti_studenta(self, studentas):
        self.studentu_sarasas
studentu_sistema = StudentuValdymoSistema()
studentas1 = Studentas("Jonas", "Jonaitis, 23, 102, [6,8,9]")
studentai.prideti_pazymi(5)
studentai.prideti_pazymi(7)
studentai.prideti_pazymi(1)

print(studentas1.studento_informacija())
studentas1.pasaliti_pazymi()
print(studentas1.studento_informacija)