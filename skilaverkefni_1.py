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
            if teljari % 4 == 0:
                print("\n")
            if x >= 1 and x <= 250:
                teljari3 += 1
            if x >= 251 and x <= 500:
                teljari4 += 1

        print("Minnsta talan er:", min(randomlisti))
        print("Stærsta talan er:", max(randomlisti))

        for x in randomlisti[::-1]:
            teljari2 += 1
            print(x, end=" ")
            if teljari2 % 6 == 0:
                print("\n")
        print("\nÞað voru", teljari3, "tölur á bilinu 1-250")
        print("Það voru", teljari4, "tölur á bilinu 251-500")

    elif valm == "3":
        print("Þú hefur valið Verkefni 3")


        nafnalisti = []
        print("Sláðu inn 5 nöfn fyrir neðan")
        for x in range(5):
            nafn = input("")
            nafnalisti.append(nafn)

        #valmynd
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
                for x in nafnalisti:
                    print(x)#birtir listann

            elif valm == "2":
                radadur = nafnalisti.sort()
                print(radadur)

