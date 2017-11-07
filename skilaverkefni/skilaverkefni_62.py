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
class Bardagi:
    def brdgi(self, lid1, lid2):
        herdeild1 = []
        herdeild2 = []

        for x in lid1:
            herdeild1.append(x)
        for x in lid2:
            herdeild2.append(x)

        teljari = 0

        while teljari == 0:
            for x, y in zip(herdeild1, herdeild2):
                # print(x, "og", y)

                # spjot
                if "spjot" in x and "sverð" in y:
                    print(x, "er sterkari en", y, "og", y, "tapar", x[14], "stig af lífinu sínu")
                    # herdeild1.append(x) #setur x i aframlid1
                    if x[14] <= y[8]:  # ef afl fra x er minna en lif hja y
                        damage = int(y[8]) - int(x[14])  # lif y minus afl x
                        if damage > 0:
                            yListi = list(y)  # setur y upp sem lista
                            yListi[8] = damage
                            strengur = "".join(map(str, yListi))  # breytir yListi aftur i streng
                            herdeild2.append(strengur)  # setur strengur i aframLid2
                            herdeild2.remove(y)
                        else:
                            herdeild2.remove(y)
                    else:
                        herdeild2.remove(y)

                if "spjot" in x and "exi" in y:
                    print(x, "tapar á móti", y, "og", x, "tapar", y[12], "stig af lífinu sínu")
                    # herdeild2.append(y)
                    if y[12] <= x[8]:  # ef afl fra y er minna en lif hja x
                        damage = int(x[8]) - int(y[12])  # lif x minus afl y
                        if damage > 0:
                            xListi = list(x)  # set x upp sem lista
                            xListi[8] = damage
                            strengur = "".join(map(str, xListi))  # breytir xListi aftur i streng
                            herdeild1.append(strengur)  # setur strengur i aframLid1
                            herdeild1.remove(x)
                        else:
                            herdeild1.remove(x)
                    else:
                        herdeild1.remove(x)
                if "spjot" in x and "spjot" in y:
                    print(x, "og", y, "hafa báðir exi og taka báðir skaða")
                    lif1 = int(x[8])
                    lif2 = int(y[8])
                    afl1 = int(x[14])
                    afl2 = int(y[14])

                    if afl1 > lif2:
                        print(y, "tapar a moti", x)
                        herdeild2.remove(y)
                    elif afl1 < lif2:
                        damage = lif2 - afl1
                        if damage > 0:
                            yListi = list(y)
                            yListi[8] = damage
                            strengur = "".join(map(str, yListi))
                            herdeild2.append(strengur)
                            herdeild2.remove(y)
                        else:
                            herdeild2.remove(y)
                    else:
                        herdeild2.remove(y)

                    if afl2 > lif1:
                        print(x, "tapar a moti", y)
                        herdeild1.remove(x)
                    elif afl2 < lif1:
                        damage = lif1 - afl2
                        if damage > 0:
                            xListi = list(x)
                            xListi[8] = damage
                            strengur = "".join(map(str, xListi))
                            herdeild1.append(strengur)
                            herdeild1.remove(x)
                        else:
                            herdeild1.remove(x)
                    else:
                        herdeild1.remove(x)

                # sverð
                if "sverð" in x and "spjot" in y:
                    print(x, "tapar á móti", y, "og", x, "tapar", y[14], "stig af lífinu sínu")
                    # herdeild2.append(y)
                    if y[14] <= x[8]:
                        damage = int(x[8]) - int(y[14])
                        if damage > 0:
                            xListi = list(x)
                            xListi[8] = damage
                            strengur = "".join(map(str, xListi))
                            herdeild1.append(strengur)
                            herdeild1.remove(x)
                        else:
                            herdeild1.remove(x)
                    else:
                        herdeild1.remove(x)

                if "sverð" in x and "exi" in y:
                    print(x, "er sterkari en", y, "og", y, "tapar", x[14], "stig af lífinu sínu")
                    # herdeild1.append(x)
                    if x[14] <= y[8]:
                        damage = int(y[8]) - int(x[14])
                        if damage > 0:
                            yListi = list(y)
                            yListi[8] = damage
                            strengur = "".join(map(str, yListi))
                            herdeild2.append(strengur)
                            herdeild2.remove(y)
                        else:
                            herdeild2.remove(y)
                    else:
                        herdeild2.remove(y)
                if "sverð" in x and "sverð" in y:
                    print(x, "og", y, "hafa báðir exi og taka báðir skaða")
                    lif1 = int(x[8])
                    lif2 = int(y[8])
                    afl1 = int(x[14])
                    afl2 = int(y[14])

                    if afl1 > lif2:
                        print(y, "tapar a moti", x)
                        herdeild2.remove(y)
                    elif afl1 < lif2:
                        damage = lif2 - afl1
                        if damage > 0:
                            yListi = list(y)
                            yListi[8] = damage
                            strengur = "".join(map(str, yListi))
                            herdeild2.append(strengur)
                            herdeild2.remove(y)
                        else:
                            herdeild2.remove(y)
                    else:
                        herdeild2.remove(y)

                    if afl2 > lif1:
                        print(x, "tapar a moti", y)
                        herdeild1.remove(x)
                    elif afl2 < lif1:
                        damage = lif1 - afl2
                        if damage > 0:
                            xListi = list(x)
                            xListi[8] = damage
                            strengur = "".join(map(str, xListi))
                            herdeild1.append(strengur)
                            herdeild1.remove(x)
                        else:
                            herdeild1.remove(x)
                    else:
                        herdeild1.remove(x)

                # exi
                if "exi" in x and "sverð" in y:
                    print(x, "tapar á móti", y, "og", x, "tapar", y[14], "stig af lífinu sínu")
                    # herdeild2.append(y)
                    if y[14] <= x[8]:  # ef afl y er minna en lif x
                        damage = int(x[8]) - int(y[14])  # lif x minus afl y
                        if damage > 0:
                            xListi = list(x)
                            xListi[8] = damage
                            strengur = "".join(map(str, xListi))
                            herdeild1.append(strengur)
                            herdeild1.remove(x)
                        else:
                            herdeild1.remove(x)
                    else:
                        herdeild1.remove(x)
                if "exi" in x and "spjot" in y:
                    print(x, "er sterkari en", y, "og", y, "tapar", x[12], "stig af lífinu sínu")
                    # herdeild1.append(x)
                    if x[12] <= y[8]:  # ef afl x er minna en lif y
                        damage = int(y[8]) - int(x[12])  # lif y minus afl x
                        if damage > 0:
                            yListi = list(y)
                            yListi[8] = damage
                            strengur = "".join(map(str, yListi))
                            herdeild2.append(strengur)
                            herdeild2.remove(y)
                        else:
                            herdeild2.remove(y)
                    else:
                        herdeild2.remove(y)

                if "exi" in x and "exi" in y:
                    print(x, "og", y, "hafa báðir exi og taka báðir skaða")
                    lif1 = int(x[8])
                    lif2 = int(y[8])
                    afl1 = int(x[12])
                    afl2 = int(y[12])

                    if afl1 > lif2:
                        print(y, "tapar a moti", x)
                        herdeild2.remove(y)
                    elif afl1 < lif2:
                        damage = lif2 - afl1
                        if damage > 0:
                            yListi = list(y)
                            yListi[8] = damage
                            strengur = "".join(map(str, yListi))
                            herdeild2.append(strengur)
                            herdeild2.remove(y)
                        else:
                            herdeild2.remove(y)
                    else:
                        herdeild2.remove(y)

                    if afl2 > lif1:
                        print(x, "tapar a moti", y)
                        herdeild1.remove(x)
                    elif afl2 < lif1:
                        damage = lif1 - afl2
                        if damage > 0:
                            xListi = list(x)
                            xListi[8] = damage
                            strengur = "".join(map(str, xListi))
                            herdeild1.append(strengur)
                            herdeild1.remove(x)
                        else:
                            herdeild1.remove(x)
                    else:
                        herdeild1.remove(x)

            if len(herdeild1) == 0:
                teljari += 1
            elif len(herdeild2) == 0:
                teljari += 1

        # sjaum utkomurnar

        print("Thad eru", len(herdeild1), "eftir af herdeild1:", *herdeild1)
        print("Thad eru", len(herdeild2), "eftir af herdeild2:", *herdeild2)


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

bardagi = Bardagi()
bardagi.brdgi(herdeildA, herdeildB)



