#24.8.2017
#Ingvar Vigfússon
#Upprifjun 2

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

        fNafn=input("Fyrra nafn: ")
        fHaed=int(input("Hæð í sentimetrum: "))
        sNafn=input("Seinna nafn: ")
        sHaed=int(input("Hæð í sentimetrum: "))


        if fHaed > sHaed:
            print(fNafn, "er stærri en", sNafn)
        if sHaed > fHaed:
            print(sNafn, "er stærri en", fNafn)
        if sHaed == fHaed:
            print(fNafn, "og", sNafn, "eru jafnhá")

    if valm == "2":
        print("Þú hefur valið dæmi 2")

        lengd=int(input("Lengd reits í metrum: "))
        breidd=int(input("Breidd reits í metrum: "))

        form = (lengd * breidd) / 4046
        utkoma = round(form, 3)

        print("Þessi reitur er", utkoma, "ekrur")

    if valm == "3":
        print("Þú hefur valið dæmi 3")

        breidd=int(input("Breidd fernings í metrum: "))
        print("Stærð    Lengd í ekrum")

        for x in range(10, 200, 10):
            form = (breidd * x) / 4046
            utkoma = round(form, 6)
            print(x, "     ", utkoma)

    if valm == "4":
        print("Þú hefur valið dæmi 4")

        afangi=input("Skammstöfun áfanga: ")

        stafir = afangi[:3]
        tolur = afangi[4:7]
        stafirU = stafir.upper()
        if len(afangi) == 7:
            if stafir == stafirU:
                print("Þetta er rétt skammstöfun")
            else:
                print("Þetta er ekki rétt skammstöfun")


        else:
            print("Þetta er ekki rétt skammstöfun")

    if valm == "5":
        print("Þú hefur valið dæmi 5")

        heild=int(input("Hver er heildin? "))
        prosenta=int(input("Hver er %? "))

        form = prosenta / 100
        reikn = heild * form

        print("Niðurstaða:", reikn)




















