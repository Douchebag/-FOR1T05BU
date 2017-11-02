#2.11.2017
#Ingvar Vigfússon
#Skilaverkefni 6

import random

class Hermann:
    def __init__(self, lif, afl, avopn, teljari):


        self.lid1 = []
        self.lid2 = []

        self.lid1.append("lid1_h" + str(teljari) + "(" + str(lif) + vopn + str(afl) + ")")
        self.lid2.append("lid2_h" + str(teljari) + "(" + str(lif) + vopn + str(afl) + ")")

    def lid_1(self):
        for x in self.lid1:
            return x
    def lid_2(self):
        for x in self.lid2:
            return x
    def bardagi(self):
        for x, y in zip(self.lid_1(), self.lid_2()):
            return x, "á móti", y


#dæmi 1
herdeildA = []
herdeildB = []

teljari = 0
for x in range(5):
    teljari += 1
    lif = random.randint(1, 5)
    afl = random.randint(1, 5)
    vopn = random.randint(1, 3)
    if vopn == 1:
        vopn = "sverð"
    elif vopn == 2:
        vopn = "spjot"
    elif vopn == 3:
        vopn = "exi"
    lid1 = Hermann(lif, afl, vopn, teljari)
    herdeildA.append(lid1.lid_1())

teljari = 0
for i in range(5):
    teljari += 1
    lif = random.randint(1, 5)
    afl = random.randint(1, 5)
    vopn = random.randint(1, 3)
    if vopn == 1:
        vopn = "sverð"
    elif vopn == 2:
        vopn = "spjot"
    elif vopn == 3:
        vopn = "exi"
    lid2 = Hermann(lif, afl, vopn, teljari)
    herdeildB.append(lid2.lid_2())

#exi > spjot > sverð > exi
#spjot vinnur sverð
#sverð vinnur exi
#exi vinnur spjot

for x, y in zip(herdeildA, herdeildB):  # keyrir í gegnum herraTupla og domurTupla samtímis
    #print(x, "og", y)

    #spjot
    if "spjot" in x and "sverð" in y:
        print(x, "er sterkari en", y, "og", y, "tekur", x[14], "stig af lífinu sínu")
    if "spjot" in x and "exi" in y:
        print(x, "tapar á móti", y, "og", x, "tapar", y[12], "stig af lífinu sínu")
    if "spjot" in x and "spjot" in y:
        print(x, "og", y, "hafa báðir spjót og enginn tekur skaða")

    #sverð
    if "sverð" in x and "spjot" in y:
        print(x, "tapar á móti", y, "og", x, "tapar", y[14], "stig af lífinu sínu")
    if "sverð" in x and "exi" in y:
        print(x, "er sterkari en", y, "og", y, "tapar", x[14], "stig af lífinu sínu")
    if "sverð" in x and "sverð" in y:
        print(x, "og", y, "hafa báðir sverð og enginn tekur skaða")

    #exi
    if "exi" in x and "sverð" in y:
        print(x, "tapar á móti", y, "og", x, "tapar", y[14], "stig af lífinu sínu")
    if "exi" in x and "spjot" in y:
        print(x, "er sterkari en", y, "og", y, "tapar", x[12], "stig af lífinu sínu")
    if "exi" in x and "exi" in y:
        print(x, "og", y, "hafa báðir exi og enginn tekur skaða")