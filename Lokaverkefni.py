#21.11.2017
#Ingvar Vigfússon & Sigurður Róbert
#Lokaverkefni: Nagdýr

from random import randint, randrange
'''
nd1Stad = 0
nd1Afl = randrange(2, 7, 2)
nd1 = ["mus", nd1Stad, nd1Afl]

print(nd1Afl)


while nd1Stad < 100:
    nd1Stad += randint(1, 6)
    nd1.remove(nd1[1])
    nd1.append(nd1Stad)
    print(nd1)
    print(nd1Stad)

#Það sem fer inní Nagdyr smiðinn
teljari = 0
nd1Teg = randint(1, 3)
if nd1Teg == 1:
    nd1Teg = "mus"
elif nd1Teg == 2:
    nd1Teg = "rotta"
elif nd1Teg == 3:
    nd1Teg = "hamstur"
'''

class Nagdyr:
    def __init__(self, tegund, stadsetning, afl):
        self.teg = tegund
        self.stad = stadsetning
        self.afl = afl
    def uppl(self):
        return "Ég er " + self.teg + " afl: " + str(self.afl) + " stad: " + str(self.stad)

musStad = 0
musAfl = randrange(2, 7, 2)
#rottur
r1Stad = randint(1, 100)
r1Afl = randrange(2, 7, 2)
r2Stad = randint(1, 100)
r2Afl = randrange(2, 7, 2)
r3Stad = randint(1, 100)
r3Afl = randrange(2, 7, 2)
#hamstur
hamStad = randint(1, 100)
hamAfl = randrange(2, 7, 2)

teljari = 0
kast = randint(1, 6)
while musStad < 100:
    #hreyfing fyrir mús
    for i in range(randint(1, 6)):
        musStad += 1
        if musStad == r1Stad:
            if musAfl < r1Afl:
                for x in range(randint(1, 6)):
                    musStad += 1
                musStad -= r1Afl
        elif musStad == r2Stad:
            if musAfl < r2Afl:
                for x in range(randint(1, 6)):
                    musStad += 1
                musStad -= r2Afl
        elif musStad == r3Stad:
            if musAfl < r3Afl:
                for x in range(randint(1, 6)):
                    musStad += 1
                musStad -= r3Afl
    # 1 er áfram og 2 er afturábak
    for i in range(randint(1, 6)):
        attir = randint(1, 2)
        if attir == 1:
            r1Stad += 1
            if r1Stad == musStad:
                if musAfl < r1Afl:
                    for x in range(r1Afl):
                        musStad -= 1
        elif attir == 2:
            r1Stad -= 1
            if r1Stad == musStad:
                if musAfl < r1Afl:
                    for x in range(r1Afl):
                        musStad -= 1

    mus = Nagdyr("mus", musStad, musAfl)

    rotta1 = Nagdyr("rotta1", r1Stad, r1Afl)
    rotta2 = Nagdyr("rotta2", r2Stad, r2Afl)
    rotta3 = Nagdyr("rotta3", r3Stad, r3Afl)

    hamstur = Nagdyr("hamstur", hamStad, hamAfl)

    print(mus.uppl())
    print(rotta1.uppl())
    print(rotta2.uppl())
    print(rotta3.uppl())

    teljari += 1

print(teljari)
