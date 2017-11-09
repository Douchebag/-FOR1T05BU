#31.10.2017
#Ingvar Vigfússon
#Skilaverkefni 5 klasar
import math
import random

#dæmi 1
class Hringur:
    def hUmmal(self, radius):
        ummal = 2 * radius * math.pi
        return ummal
    def hFlatarm(self, radius):
        flatarmal = 2 * (radius * radius) * math.pi
        return flatarmal
    def kRummal(self, radius):
        rummal = 3 * ((radius * radius * radius) * math.pi) / 4
        return rummal

class Jofnur:
    def fyrra(self, x):
        y = (3 * (x)) + 4 + ((2 * x)**3)
        return y
    def seinni(self, x, z):
        y = ((z)**2 + (x)**2) * 4
        return y

#dæmi 2
class Hnit:
    def __init__(self, x, y):
        self.x_hnit = x
        self.y_hnit = y
    def hnitSkrif(self):
        print("x hnitið er", self.x_hnit, "og y hnitið er", self.y_hnit)
    def hnitakerfi(self):
        if self.x_hnit >= 0 and self.y_hnit >= 0:
            return "Punkturinn er í 1. fjórðung"
        elif self.x_hnit <= 0 and self.y_hnit >= 0:
            return "Punkturinn er í 2. fjórðung"
        elif self.x_hnit <= 0 and self.y_hnit <= 0:
            return "Punkturinn er í 3. fjórðung"
        elif self.x_hnit >= 0 and self.y_hnit <= 0:
            return "Punkturinn er í 4. fjórðung"

class Hnit2:
    def __init__(self, x, y):
        self.x_hnit = x
        self.y_hnit = y

    def hnitSkrif(self):
        print("x hnitið er", self.x_hnit, "og y hnitið er", self.y_hnit)
    def hnitakerfi(self):
        if self.x_hnit >= 0 and self.y_hnit >= 0:
            return "Punkturinn er í 1. fjórðung"
        elif self.x_hnit <= 0 and self.y_hnit >= 0:
            return "Punkturinn er í 2. fjórðung"
        elif self.x_hnit <= 0 and self.y_hnit <= 0:
            return "Punkturinn er í 3. fjórðung"
        elif self.x_hnit >= 0 and self.y_hnit <= 0:
            return "Punkturinn er í 4. fjórðung"

#dæmi 1
rad = Hringur()

print(round(rad.hUmmal(2), 2))
print(round(rad.hFlatarm(2), 2))
print(round(rad.kRummal(2), 2))
print("--------------------")

#jofnur
y = Jofnur()
rTala = random.randint(-10, 10)
rTala1 = random.randint(-10, 10)
rTala2 = random.randint(-10, 10)

print(y.fyrra(rTala), "= 3 *", rTala, "+ 4 + 2 *", str(rTala) + "³")
print(y.seinni(rTala1, rTala2), "= (" + str(rTala2) + "² +", str(rTala1) + "²) * 4")
print("--------------------")

#dæmi 2
r1 = random.randint(-10, 10)
r2 = random.randint(-10, 10)
r3 = random.randint(-10, 10)
r4 = random.randint(-10, 10)

rand = Hnit(r1, r2)
rand2 = Hnit(r3, r4)

rand.hnitSkrif()
print(rand.hnitakerfi())
print("--------------------")
rand2.hnitSkrif()
print(rand2.hnitakerfi())


lengd = math.sqrt(abs(rand.x_hnit - rand2.x_hnit)**2 + abs(rand.y_hnit - rand2.y_hnit)**2)
print("Stysta leiðin milli punktana er:", round(lengd, 2))

