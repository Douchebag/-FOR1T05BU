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
#teljarar
teljari = 0
kastTeljari = 0
r1Teljari = 0
r2Teljari = 0
r3Teljari = 0
hamTeljari = 0
hundradTeljari = 0 #notad svo mus fer ekki yfir 100

#get notad t.d. mus.stad i stað musStad og mus.afl etc
#þarf að bua til nagdyrin fyrst
'''
mus = Nagdyr("mus", musStad, musAfl)

rotta1 = Nagdyr("rotta1", r1Stad, r1Afl)
rotta2 = Nagdyr("rotta2", r2Stad, r2Afl)
rotta3 = Nagdyr("rotta3", r3Stad, r3Afl)

hamstur = Nagdyr("hamstur", hamStad, hamAfl)
'''

svar = ""
while musStad < 100:
    svar = input("Villtu kasta tening? Y/N ").upper()
    if svar == "Y":
        #hreyfing fyrir mús
        for i in range(randint(1, 6)):
            musStad += 1
            if musStad > 99:
                hundradTeljari += 1

            kastTeljari += 1
            if musStad == r1Stad:
                print("Músin lenti á sama reit og Rotta 1. Reitur:", musStad)
                if musAfl < r1Afl:
                    print("Afl rottunar er stærri svo músinni er ýtt", r1Afl, "tilbaka")
                    if musStad - r1Afl < 0:
                        musStad = 0 # svo musStad fer ekki í mínus
                    else:
                        musStad -= r1Afl
            elif musStad == r2Stad:
                print("Músin lenti á sama reit og Rotta 2. Reitur:", musStad)
                if musAfl < r2Afl:
                    print("Afl rottunar er stærri svo músinni er ýtt", r1Afl, "tilbaka")
                    if musStad - r2Afl < 0:
                        musStad = 0 #svo musSTad fer ekki i minus
                    else:
                        musStad -= r2Afl
            elif musStad == r3Stad:
                print("Músin lenti á sama reit og Rotta 3. Reitur:", musStad)
                if musAfl < r3Afl:
                    print("Afl rottunar er stærri svo músinni er ýtt", r1Afl, "tilbaka")
                    if musStad - r3Afl < 0:
                        musStad = 0 #svo musStaf fer ekki i minus
                    else:
                        musStad -= r3Afl
            elif musStad == hamStad:
                print("Músin lenti á sama reit og Hamsturinn. Reitur:", musStad, "og er ýtt", hamAfl, "áfram")
                musStad += hamAfl # sleppir rottum
                if (musStad - hamStad) > 0:
                    hamStad += hamAfl/2 # hamsturinn fer sömu átt og músin sem nemur hálfu afli hans.
                elif (musStad - hamStad) < 0:
                    hamStad -= hamAfl/2 # hamsturinn fer sömu átt og músin sem nemur hálfu afli hans.
        print("Músin kastaði tening og fékk", kastTeljari)
        kastTeljari = 0 #reset fyrir kast teljarann

        # hreyfing rottu 1
        for i in range(randint(1, 6)):
            r1Teljari += 1
            attir = randint(1, 2) # 1 er áfram og 2 er afturábak
            if attir == 1:
                r1Stad += 1
                if r1Stad == musStad: #ef stadsetning rottu 1 er sama og mus
                    if musAfl < r1Afl: #ef afl rottunar er staerra en afl musarinnar
                        for x in range(r1Afl):
                            musStad -= 1
                    elif musAfl > r1Afl: #ef afl musarinnar er staerra en afl rottunar +2 fyrir mus
                        for x in range(2):
                            musStad += 1
                elif r1Stad == hamStad: #ef stadsetning rottu 1 er sama og hamstur
                    r1Stad -= 1 # minus thvi hun kom i plus
                    hamStad += 1 # hamstur faer 1 i hina attina

            elif attir == 2:
                if r1Stad < 1:
                    r1Stad += 1
                elif r1Stad > 1:
                    r1Stad -= 1
                if r1Stad == musStad:
                    if musAfl < r1Afl: #ef afl rottunar er staerra en afl musarinnar
                        for x in range(r1Afl):
                            musStad -= 1
                    elif musAfl > r1Afl: #ef afl musarinnar er staerra en afl rottunar +2 fyrir mus
                        for x in range(2):
                            musStad += 1
                elif r1Stad == hamStad: #ef stadsetning rottu 1 er sama og hamstur
                    r1Stad += 1 # plus thvi hun kom i minus
                    hamStad -= 1  # hamstur faer 1 i hina attina
        print("Rotta 1 fékk", r1Teljari, "á teningakasti sínu")
        r1Teljari = 0 # reset fyrir r1 teljarann

        #hreyfing fyrir rottu 2
        for i in range(randint(1, 6)):
            r2Teljari += 1
            attir = randint(1, 2) # 1 er áfram og 2 er afturábak
            if attir == 1:
                r2Stad += 1
                if r2Stad == musStad: #ef stadsetning rottu 1 er sama og mus
                    if musAfl < r2Afl: #ef afl rottunar er staerra en afl musarinnar
                        for x in range(r2Afl):
                            musStad -= 1
                    elif musAfl > r2Afl: #ef afl musarinnar er staerra en afl rottunar +2 fyrir mus
                        for x in range(2):
                            musStad += 1
                elif r2Stad == hamStad: #ef stadsetning rottu 1 er sama og hamstur
                    r2Stad -= 1 # minus thvi hun kom i plus
                    hamStad += 1 # hamstur faer 1 i hina attina

            elif attir == 2:
                if r2Stad < 1:
                    r2Stad += 1
                elif r2Stad > 1:
                    r2Stad -= 1
                if r2Stad == musStad:
                    if musAfl < r2Afl: #ef afl rottunar er staerra en afl musarinnar
                        for x in range(r2Afl):
                            musStad -= 1
                    elif musAfl > r2Afl: #ef afl musarinnar er staerra en afl rottunar +2 fyrir mus
                        for x in range(2):
                            musStad += 1
                elif r2Stad == hamStad: #ef stadsetning rottu 1 er sama og hamstur
                    r2Stad += 1 # plus thvi hun kom i minus
                    hamStad -= 1  # hamstur faer 1 i hina attina
        print("Rotta 2 fékk", r2Teljari, "á teningakasti sínu")
        r2Teljari = 0 #reset

        # hreyfing fyrir rottu 3
        for i in range(randint(1, 6)):
            r3Teljari += 1
            attir = randint(1, 2) # 1 er áfram og 2 er afturábak
            if attir == 1:
                r3Stad += 1
                if r3Stad == musStad: #ef stadsetning rottu 1 er sama og mus
                    if musAfl < r3Afl: #ef afl rottunar er staerra en afl musarinnar
                        for x in range(r3Afl):
                            musStad -= 1
                    elif musAfl > r3Afl: #ef afl musarinnar er staerra en afl rottunar +2 fyrir mus
                        for x in range(2):
                            musStad += 1
                elif r3Stad == hamStad: #ef stadsetning rottu 1 er sama og hamstur
                    r3Stad -= 1 # minus thvi hun kom i plus
                    hamStad += 1 # hamstur faer 1 i hina attina

            elif attir == 2:
                if r3Stad < 1:
                    r3Stad += 1
                elif r3Stad > 1:
                    r3Stad -= 1
                if r3Stad == musStad:
                    if musAfl < r3Afl: #ef afl rottunar er staerra en afl musarinnar
                        for x in range(r3Afl):
                            musStad -= 1
                    elif musAfl > r3Afl: #ef afl musarinnar er staerra en afl rottunar +2 fyrir mus
                        for x in range(2):
                            musStad += 1
                elif r3Stad == hamStad: #ef stadsetning rottu 1 er sama og hamstur
                    r3Stad += 1 # plus thvi hun kom i minus
                    hamStad -= 1  # hamstur faer 1 i hina attina
        print("Rotta 3 fékk", r3Teljari, "á teningakasti sínu")
        r3Teljari = 0  # reset

        #hreyfing fyrir hamstur
        for i in range(randint(1, 6)):
            if (musStad - hamStad) > 0:
                hamStad += 1
            elif (musStad - hamStad) < 0:
                hamStad -= 1
        if hamStad == musStad:
            print("Hamsturinn lenti á sama reit og stoppar")
            hamStad = musStad

        musStad = musStad - hundradTeljari
        hundradTeljari = 0

        mus = Nagdyr("mus", musStad, musAfl)

        rotta1 = Nagdyr("rotta1", r1Stad, r1Afl)
        rotta2 = Nagdyr("rotta2", r2Stad, r2Afl)
        rotta3 = Nagdyr("rotta3", r3Stad, r3Afl)

        hamstur = Nagdyr("hamstur", hamStad, hamAfl)

        print(mus.uppl())
        print(rotta1.uppl())
        print(rotta2.uppl())
        print(rotta3.uppl())
        print(hamstur.uppl())

        teljari += 1

print("Það tók", teljari, "teninga köst til að komast í 100")
