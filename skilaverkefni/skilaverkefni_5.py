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

class Hermann:
    def lif(self):
        lif = random.randint(1, 5)
        return lif
    def vopn(self):
        vopn = random.randint(1, 3)
        if vopn == 1:
            return "sverd"
        elif vopn == 2:
            return "spjot"
        elif vopn == 3:
            return "exi"
    def afl(self):
        afl = random.randint(1, 5)
        return afl

    '''
    lid1 = []
    lid2 = []
    teljari = 0

    for x in range(10):
        teljari += 1
        if teljari % 2 == 0:
            lid1.append("lid1_h" + str(x))
        else:
            lid2.append("lid2_h" + str(x))'''





#dæmi 1
rad = Hringur()

print(round(rad.hUmmal(2), 2))
print(round(rad.hFlatarm(2), 2))
print(round(rad.kRummal(2), 2))

#dæmi 2
r1 = random.randint(-10, 10)
r2 = random.randint(-10, 10)
r3 = random.randint(-10, 10)
r4 = random.randint(-10, 10)

rand = Hnit(r1, r2)
rand2 = Hnit2(r3, r4)

rand.hnitSkrif()
print(rand.hnitakerfi())
print("--------------------")
rand2.hnitSkrif()
print(rand2.hnitakerfi())


lengd = math.sqrt(abs(r1-r3)**2 + abs(r2-r4)**2)
print("Stysta leiðin milli punktana er:", round(lengd, 2))

#dæmi 3
lid1 = ["lid1_h1", "lid1_h2", "lid1_h3", "lid1_h4", "lid1_h5"]
lid2 = ["lid2_h1", "lid2_h2", "lid2_h3", "lid2_h4", "lid2_h5"]