from random import randint, randrange
musStad = 5
musAfl = 1
#rottur
r1Stad = 8
r1Afl = 3


teljari = 0
kast = randint(1, 6)
svar = ""
while musStad < 100:
    svar = input("Villtu kasta tening? Y/N ").upper()
    if svar == "Y":
        print(musAfl)
        print(r1Afl)
        print()
        #hreyfing fyrir mús
        for i in range(5):
            musStad += 1
            print(musStad)
            if musStad == r1Stad:
                if musAfl < r1Afl:
                    musStad -= r1Afl
        print(musStad)