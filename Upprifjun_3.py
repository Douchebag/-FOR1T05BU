#24.8.2017
#Ingvar Vigfússon
#Upprifjun 3
import datetime
#Valmynd
valm=""
while valm !="4":
    print("\n--------------")
    print("Dæmi. 1")
    print("Dæmi. 2")
    print("Dæmi. 3")
    print("Hætta. 4")
    print("--------------")
    valm=input("")

    if valm == "1":
        print("Þú hefur valið dæmi 1")
        print("Sláðu inn þrjár tölur")

        tala1 = int(input(""))
        tala2 = int(input(""))
        tala3 = int(input(""))

        if tala1 > tala2 and tala3:
            if tala2 > tala3:
                print(tala1, tala2, "og", tala3)
            elif tala3 > tala2:
                print(tala1, tala3, "og", tala2)

        elif tala2 > tala3 and tala1:
            if tala1 > tala3:
                print(tala2, tala1, "og", tala3)
            elif tala3 > tala1:
                print(tala2, tala3, "og", tala1)

        elif tala3 > tala1 and tala2:
            if tala1 > tala2:
                print(tala3, tala1, "og", tala2)
            elif tala2 > tala1:
                print(tala3, tala2, "og", tala1)
        else:
            print("Allar tölurnar eru eins")

    if valm == "2":
        print("Þú hefur valið dæmi 2")

        nafn = input("Hvað heitir þú: ")
        aldur = int(input("Hver er aldur þinn:"))

        now = datetime.datetime.now()

        reikn = 2100 - now.year + aldur

        print(nafn, ", um næstu aldamót verður þú", reikn, "ára")

    if valm == "3":
        print("Þú hefur valið dæmi 3")

        listi = []
        n0ll = ""
        while n0ll != 0:
            n0ll = int(input("Sláðu inn tölu "))
            listi.append(n0ll)

            if n0ll == 0:
                listi.remove(0)
                medaltal = sum(listi) / len(listi)
                utkoma = round(medaltal, 2)
                print("Summa listans:", sum(listi))
                print("Fjöldi talna inní listanum:", len(listi))
                print("Meðaltal listans:", utkoma)
















