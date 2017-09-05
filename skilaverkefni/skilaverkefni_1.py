#31.8.2017
#Ingvar Vigfusson
#Skilaverkefni 1
from random import *
#Valmynd
valm=""
while valm !="6":
    print("\n--------------")
    print("Verkefni. 1")
    print("Verkefni. 2")
    print("Verkefni. 3")
    print("Verkefni. 4")
    print("Verkefni. 5")
    print("Hætta. 6")
    print("--------------")
    valm=input("")

    if valm == "1":
        print("Þú hefur valið Verkefni 1")

        teljari = 0
        seinniListi = [] #listi fyrir tölur undir 50.5
        talnalisti = [] #listinn
        print("Sláðu inn 7 tölur fyrir neðan")
        for x in range(7): #keyrir for lykkjuna 7 sinnum fyrir 7 tölur
            tala = int(input("")) #tekur inn töluna
            talnalisti.append(tala) #bætir tölunni inní listann

        #finnur út meðaltal, summu, stærstu og minnstu töluna
        medaltal = sum(talnalisti) / 7
        summa = sum(talnalisti)
        staersta = max(talnalisti)
        minnsta = min(talnalisti)
        #birtir allt
        print("Meðaltal listans er:", round(medaltal, 2))
        print("Summa listans er:", summa)
        print("Stærsta tala listans er:", staersta)
        print("Minnsta tala listans er:", minnsta)
        #for slaufu fyrir að sýna listann
        for x in talnalisti: #keyrir í gegnum listann
            print(x, end=";") #birtir x, sem er hver tala í listanum með ; á milli
            if x <= 50.5: #ef x er minna eða jafnt og
                teljari += 1 #bætir við einum í teljarann
                seinniListi.append(x) #bætir þessum tölum í annan lista
        print("\nÞessar eru fyrir neðan 50,5:")
        for x in seinniListi: #keyrir í gegnum seinni listann
            print(x, end=";") #birtir tölurnar í seinni listanum
        print("\nÞað eru", teljari, "tölur sem eru minnir en 50.5")

    elif valm == "2":
        print("Þú hefur valið Verkefni 2")

        teljari = 0
        teljari2 = 0
        teljari3 = 0
        teljari4 = 0
        randomlisti = [] #listi fyrir tölrunar
        for x in range(70): #keyrir slaufuna 70 sinnum
            tala = randint(1, 500) #gefur okkur random tölu
            randomlisti.append(tala) #bætir tölunni inní listann

        for x in randomlisti:
            teljari += 1
            print(x, end=" ")
            if teljari % 4 == 0: #ef þú deilir teljaranum með 4 og ferð 0 afgangs
                print("\n")
            if x >= 1 and x <= 250: #ef x er a bilin 1 og 250
                teljari3 += 1
            if x >= 251 and x <= 500: #ef x er a bilinu 251 og 500
                teljari4 += 1

        print("Minnsta talan er:", min(randomlisti))#birtir minnstu töluna í listanum
        print("Stærsta talan er:", max(randomlisti))#birtir hæstu töluna í listanum

        for x in randomlisti[::-1]: #keyrir forlykkjuna öfugt
            teljari2 += 1 #bætir við 1 í teljari2
            print(x, end=" ")#birtir x með bil á milli í staðs línu
            if teljari2 % 6 == 0:#ef þú deilir teljara2 með 6 og færð 0 afgangs
                print("\n")#birtir nýja línu
        print("\nÞað voru", teljari3, "tölur á bilinu 1-250")#birtir svar
        print("Það voru", teljari4, "tölur á bilinu 251-500")#birtir svar

    elif valm == "3":
        print("Þú hefur valið Verkefni 3")


        nafnalisti = []
        print("Sláðu inn 5 nöfn fyrir neðan")
        for x in range(5):#keyrir forslaufu 5 sinnum
            nafn = input("")#tekur við svari
            nafnalisti.append(nafn)#bætir svari við listans

        #ný valmynd
        valm = ""
        while valm != "5":
            print("\n--------------")
            print("1. Birta nöfnin óraðað")
            print("2. Raða nöfnunum í stafrófsröð og birta")
            print("3. Raða nöfnunum í öfuga stafrófsröð og birta")
            print("4. Birta eitt nafn eftir því hvaða númer 1-5 var valið")
            print("5. Hætta í verkefni 3")
            print("--------------")
            valm = input("")

            if valm == "1":
                for x in nafnalisti:#keyrir í gegnum listann
                    print(x)#birtir listann

            elif valm == "2":
                radadur = sorted(nafnalisti) #gildi fyrir listann eftir að hann er raðaður
                for x in radadur:#keyrir í gegnum raðaða listann
                    print(x)#birtir x

            elif valm == "3":
                ofugt = sorted(nafnalisti, reverse=True)#tekur listann og raðar honum og snýr honum við
                for x in ofugt:#keyrir í gegnum öfuga listann
                    print(x)#birtir x
            elif valm == "4":
                numerNafn = int(input("Veldu númerið á nafninu: "))

                print(nafnalisti[numerNafn-1])

    elif valm == "4":
        print("Þú hefur valið Verkefni 4")

        fjoldi = int(input("Hversu oft villtu kasta teningnum? "))#tekur við svari notanda

        teningur = []#listi fyrir tölurnar sem koma
        for x in range(fjoldi):#keyrir forslaufuna eins oft og notandinn vill
            t1 = randint(1, 6)#random tala milli 1 og 6
            print("Þú fékkst: ", t1)#birtir töluna sem kom
            teningur.append(t1)#bætir töluni við listann

        #telur stakinn í listanum, hefði getað sett upp teljara í forslaufunni
        tal1 = teningur.count(1)
        tal2 = teningur.count(2)
        tal3 = teningur.count(3)
        tal4 = teningur.count(4)
        tal5 = teningur.count(5)
        tal6 = teningur.count(6)

        #birtir hversu oft tölurnar koma upp
        print("Talan 1 kom: ", tal1, "sinnum")
        print("Talan 2 kom: ", tal2, "sinnum")
        print("Talan 3 kom: ", tal3, "sinnum")
        print("Talan 4 kom: ", tal4, "sinnum")
        print("Talan 5 kom: ", tal5, "sinnum")
        print("Talan 6 kom: ", tal6, "sinnum")

        #finur út hvaða tala kemur oftast
        if tal1 >= tal2 and tal1 >= tal3 and tal1 >= tal4 and tal1 >= tal5 and tal1 >= tal6:
            print("Talan 1 kom upp oftast")
        elif tal2 >= tal3 and tal2 >= tal4 and tal2 >= tal5 and tal2 >= tal6 and tal2 >= tal1:
            print("Talan 2 kom upp oftast")
        elif tal3 >= tal4 and tal3 >= tal5 and tal3 >= tal6 and tal3 >= tal1 and tal3 >= tal2:
            print("Talan 3 kom upp oftast")
        elif tal4 >= tal5 and tal4 >= tal6 and tal4 >= tal1 and tal4 >= tal2 and tal4 >= tal3:
            print("Talan 4 kom upp oftast")
        elif tal5 >= tal6 and tal5 >= tal1 and tal5 >= tal2 and tal5 >= tal3 and tal5 >= tal4:
            print("Talan 5 kom upp oftast")
        elif tal6 >= tal1 and tal6 >= tal2 and tal6 >= tal3 and tal6 >= tal4 and tal6 >= tal5:
            print("Talan 6 kom upp oftast")

        #finnur út töluna sem kom upp minnst
        if tal1 <= tal2 and tal1 <= tal3 and tal1 <= tal4 and tal1 <= tal5 and tal1 <= tal6:
            print("Talan 1 kom upp minnst")
        elif tal2 <= tal3 and tal2 <= tal4 and tal2 <= tal5 and tal2 <= tal6 and tal2 <= tal1:
            print("Talan 2 kom upp minnst")
        elif tal3 <= tal4 and tal3 <= tal5 and tal3 <= tal6 and tal3 <= tal1 and tal3 <= tal2:
            print("Talan 3 kom upp minnst")
        elif tal4 <= tal5 and tal4 <= tal6 and tal4 <= tal1 and tal4 <= tal2 and tal4 <= tal3:
            print("Talan 4 kom upp minnst")
        elif tal5 <= tal6 and tal5 <= tal1 and tal5 <= tal2 and tal5 <= tal3 and tal5 <= tal4:
            print("Talan 5 kom upp minnst")
        elif tal6 <= tal1 and tal6 <= tal2 and tal6 <= tal3 and tal6 <= tal4 and tal6 <= tal5:
            print("Talan 6 kom upp minnst")

    elif valm == "5":
        print("Þú hefur valið verkefni 6")

        fjoldi = int(input("Hversu margir eru skráðir í hópinn? "))#tekur við svari notandann
        nafnalisti = []#listi undir nöfnin
        print("Skrifaðu nöfnin fyrir neðan")
        for x in range(fjoldi):#keyrir forslaufuna jafn oft og notanda sagði að væru nöfn
            nafn = input("")#tekur við nafni
            nafnalisti.append(nafn)#bætir nafni í listann

        for x in sorted(nafnalisti):#keyrir í gegnum röðuðum listann
            print(x)#birtir x