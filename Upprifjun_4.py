#28.8.2017
#Ingvar Vigfusson
#Upprifjun 4
from random import *
#Valmynd
valm=""
while valm !="6":
    print("\n--------------")
    print("Dæmi. 1")
    print("Dæmi. 2")
    print("Dæmi. 3")
    print("Dæmi. 4")
    print("Dæmi. 5")
    print("Hætta. 6")
    print("--------------")
    valm=input("")

    if valm == "1":
        print("Þú hefur valið dæmi 1")

        print("Sladu inn setningu thina")
        setn = input("")

        teljari = 0
        for x in setn:
            if x == "n" or x == "N":
                teljari += 1

        print("Thad eru", teljari, "n i thessari setningu")

    elif valm == "2":
        print("Þú hefur valið dæmi 2")

        print("Sladu inn tvo nofn")
        list1 = []
        list2 = []
        nafn1 = input("Fyrsta nafn: ").upper()
        nafn2 = input("Seinna nafn: ").upper()

        for x in nafn1:
            list1.append(x)

        for x in nafn2:
            list2.append(x)

        if len(nafn1) == len(nafn2):
            print("Nöfnin eru jafn löng.")

            for x in range(len(list1)):
                if list2[x] == list1[x]:
                    print("bókstafur númer", x+1, list1[x], "er eins í báðum nöfnum.")
        else:
            print("Nöfnin eru ekki jafn löng.")

    elif valm == "3":
        print("Þú hefur valið dæmi 3")

        nafn = input("Hvert er nafnid? ")
        list1 = []
        list2 = []
        list1.append(nafn)
        list2.append(nafn[::-1])

        for x in range(len(list1)):
            if list2[x] == list1[x]:
                print("Þetta nafn er samhverfu nafn")
            else:
                print("Þetta nafn er ekki samhverfu nafn")
    elif valm == "4":
        print("Þú hefur valið dæmi 4")

        teljari = 0
        listi = []
        texti = input("Sladu inn textann thinn her: ")
        texti2 = texti.split(" ")
        texti3 = texti.replace(" ", "")
        listi.append(texti2)

        #valmynd
        valm = ""
        while valm != "8":
            print("\n--------------")
            print("1. Ordtal")
            print("2. Ord yfirfari")
            print("3. Lengd strengs")
            print("4. Snuinn texti")
            print("5. Storir stafir")
            print("6. Stafa yfirlit")
            print("7. Stort A")
            print("8. Hætta")
            print("--------------")
            valm = input("")

            if valm == "1":
                print("Þú hefur valið 1. Ordtal")
                #Finnur og skrifar út hversu mörg orð eru í textanum

                print("Thad eru", len(texti2), "ord i textanum.")

            elif valm == "2":
                print("Þú hefur valið 2. Ord yfirfari")

                #Athugaðu hvort ákveðið orð eða orðhluti er í strengnum og skrifaðu út svarið.
                yfirfari = input("Hvert er ordid sem thu villt yfirfara? ")

                for x in texti2:
                    if x == yfirfari:
                        print(x, "er i setningunni.")
                    else:
                        print(yfirfari, "er ekki i setningunni.")
            elif valm == "3":
                print("Þú hefur valið 3. Lengd strengs")
                #Segir hvað strengurinn er langur sem notandinn sló inn
                print("Strengurinn er", len(texti3), "stafa langur")

            elif valm == "4":
                print("Þú hefur valið 4. Snuinn-texti")
                #Snýr strengnum sem sleginn var inn við og prentar hann út
                print(" ".join(texti2[::-1]))

            if valm == "5":
                print("Þú hefur valið 5. Storir stafir")
                #Setur allan strenginn sem notandinn sló inn í stóra stafi og prentar út
                print(" ".join(texti2).upper())

            elif valm == "6":
                print("Þú hefur valið 6. Stafa yfirfari")
                #Biður um staf og athugar hvort hann komi fyrir í strengnum
                yfirfari = input("Hvert er ordid sem thu villt yfirfara? ")
                teljari = 0

                for x in texti3:
                    if x == yfirfari:
                        teljari += 1
                if teljari > 0:
                    print("Stafurinn er i strengnum, hann kemur fram:", teljari, "sinnum")
                else:
                    print("Stafurinn er ekki i strengnum.")

            elif valm == "7":
                print("Þú hefur valið 7. stort A")
                #Setur stórt A í staðinn fyrir öll lítil a sem koma fyrir í strengnum. Hér er gott að nota replace()
                stortA = texti.replace("a", "A")
                print(stortA)
    elif valm == "5":
        print("Þú hefur valið dæmi 5")

        hundrad = []
        teljari = 0
        teljari2 = 0
        for x in range(100):
            tala = randint(250, 400)
            hundrad.append(tala)

        medaltal = sum(hundrad) / 100
        print("Medaltalid er: ", round(medaltal, 2))

        for x in hundrad:
            if x < 267:
                teljari += 1
            if x >= 300 and x <= 350:
                teljari2 += 1
        print("Thad eru", teljari, "tolur sem eru minni en 267")

        test = hundrad.count(min(hundrad))
        print("Minnsta talan i listanum er", min(hundrad), "og hun birtist", test, "sinnum")

        print("Thad eru", teljari2, "tolur a milli 300 og 350")

        for x in hundrad:
            print(x)





