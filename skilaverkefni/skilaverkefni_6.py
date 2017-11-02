#2.11.2017
#Ingvar Vigfússon
#Skilaverkefni 6

import random

class Hermann:
    def __init__(self, lid1):
        lif = random.randint(1, 5)
        afl = random.randint(1, 5)
        vopn = random.randint(1, 3)
        if vopn == 1:
            vopn = "sverð"
        elif vopn == 2:
            vopn = "spjot"
        elif vopn == 3:
            vopn = "exi"

        lid1 = []
        lid2 = []

        for x in range(5):
            lid1.append("lid1_h" + str(x) + "(" + str(lif) + vopn + str(afl) + ")")

        return lid1

#dæmi 3
lid1 = Hermann()
print(lid1.__init__())