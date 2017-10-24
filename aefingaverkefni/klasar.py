#24.10.2017
#Ingvar Vigfússon
#Klasar æfingaverkefni

class FyrstiKlasi:
    def falleitt(self, nafn, aldur):
        print("Halló", nafn, "þú ert", aldur, "ára gamall")
    def falltvo(self, talaeitt, talatvo):
        summa = talatvo - talaeitt
        if summa >= 0:
            return summa
        elif summa <= 0:
            summa = summa * -1
            return summa

class AnnarKlassi:
    def flatarmalKassa(self, hlid1, hlid2):
        fk = hlid1 * hlid2
        return fk
    def flatarmalThri(self, lina1, lina2):
        fT = (lina1 * lina2) / 2
        return fT
    def flatarmalTrap(self, haed, hlid1, hlid2):
        fTrap = haed * ((hlid1 * hlid2) / 2)
        return fTrap

class ThridjiKlasi:
    def __init__(self, t1, t2):
        self.tala1 = t1
        self.tala2 = t2
    def leggjasaman(self):
        summa = self.tala1 + self.tala2
        return summa
    def margfalda(self):
        summa = self.tala1 * self.tala2
        return summa
    def deiling(self):
        summa = self.tala1 / self.tala2
        return summa

'''
n = "Ingvar"
a = 18
classinn = FyrstiKlasi()

classinn.falleitt(n, a)

fyrstaTalan = int(input("Hver er fyrsta talan? "))
seinniTalan = int(input("Hver er seinni talan? "))

print("Það eru", classinn.falltvo(fyrstaTalan, seinniTalan), "tölur milli þessara tveggja talna")

h1 = AnnarKlassi()
h2 = AnnarKlassi()
h3 = AnnarKlassi()

print(h1.flatarmalKassa(2,2))
print(h2.flatarmalThri(3, 4))
print(h3.flatarmalTrap(3, 5, 5))
'''

c1 = ThridjiKlasi(2, 3)
c2 = ThridjiKlasi(6, 20)
c3 = ThridjiKlasi(56, 13)
print("--------c1----------")
print(c1.leggjasaman())
print(c1.margfalda())
print(round(c1.deiling(), 2))
print("--------c2----------")
print(c2.leggjasaman())
print(c2.margfalda())
print(round(c2.deiling(), 2))
print("--------c3----------")
print(c3.leggjasaman())
print(c3.margfalda())
print(round(c3.deiling(), 2))