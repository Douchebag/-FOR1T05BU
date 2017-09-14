#12.9.2017
#Ingvar Vigfússon
#Skilaverkefni 2 föll/functions
from random import *

#föll

#fallið celsius_fahrenheit skilar celsius í fahrenheit
def celsius_fahrenheit(cels):
    farnh = cels * 1.8 + 32
    return farnh
#fallið fahrenheit_celsius skilar fahrenheit í celsius
def fahrenheit_celsius(farnh):
    cels = (farnh - 32) / 1.8
    return cels
#fallið kelvin_celsius skilar celsius í kelvin
def celsius_kelvin(cels):
    kelv = cels + 273.15
    return kelv
#fallið celsius_kelvin skilar kelvin í celsius
def kelvin_celsius(kelv):
    cels = kelv - 273.15
    return cels
#fallið grunn_veldi reiknar grunntöluna með veldisvísinum og skilar útkomuni
def grunn_veldi(grunn, veldi):
    veldid = grunn ** veldi
    return veldid
    #utkoma = 1
    #for i in range(veldi):
    #    utkoma = utkoma * grunn
        # utkoma *= grunn
    #return utkoma
#fallið tommur_sentimetra skilar tommum í sentimetrum
def tommur_sentimetrar(tomm):
    senti = tomm * 2.54
    return senti
#fallið sentimetra_tommur skilar sentimetrum í tommum
def sentimetra_tommur(senti):
    tomm = senti / 2.54
    return tomm
#gallon í lítra
def gallon_litra(gal):
    litrar = gal * 3.785
    return litrar
#litrar í gallon
def litra_gallon(litra):
    gal = litra / 3.785
    return gal
#
def nafn_kyn(nafn, kyn):
    if kyn == "KK": #ef kyn er KK
        return "Sæll og blessaður " + nafn #skilar það þessu
    elif kyn == "KVK":#annars ef kyn er KVK
        return "Sæl og blessuð " + nafn #skilar það þessari setningu
def kasta():
    randomTala = randint(1, 7)#random tala milli 1 og 7
    return randomTala#skilar randomTala
def thridjiListinn(list1, list2):
    listi3 = []

    for x in list1:#keyrir í gegnum fyrsta listann sem x
        if x in list2:#ef x er inní list2
            if x not in listi3:#og ef x er ekki nú þegar í listi3
                listi3.append(x)#bætir x inní listi3

    return listi3 #skilar listi3

#Valmynd
valm=""
while valm !="9":
    print("\n--------------")
    print("1. Breyta Celsius í Fahrenheit eða öfugt")
    print("2. Breyta Celsius í Kelvin eða öfugt")
    print("3. Grunntölur og veldi")
    print("4. Tommur og sentimetrar")
    print("5. Gallon í lítra eða öfugt")
    print("6. Nafn og kyn")
    print("7. Random heiltala 1-7")
    print("8. Lista samanburður")
    print("9. hætta")
    print("--------------")
    valm=input("")

    if valm == "1":
        print("Þú hefur valið lið 1")

        #nota .upper() til að lesa inn allt í hástöfum
        svar = input("Veldu A ef þú villt breyta Celsius í fahrenheit\neða B ef þú villt breyta Fahrenheit í Celsius ").upper()

        if svar == "A":
            hiti_c = float(input("Hvað er hitinn í Celsius? "))
            #kalla í fallið celsius_fahrenheit til að reikna
            hiti_f = celsius_fahrenheit(hiti_c)
            print(str(hiti_c) + "°C er " + format(hiti_f, ".2F") + "°F")
        elif svar == "B":
            hiti_f = float(input("Hvað er hitinn í Fahrenheit? "))
            #kalla í fallið fahrenheit_celsius til að reikna
            hiti_c = fahrenheit_celsius(hiti_f)
            print(str(hiti_f) + "°F er " + str(hiti_c) + "°C")

    elif valm == "2":
        print("Þú hefur valið lið 2")

        svar = input("Veldu A ef þú villt breyta Celsius í Kelvin\neða B ef þú villt breyta Kelvin í Celsius ").upper()

        if svar == "A":
            hiti_C = float(input("Hvað er hitinn í Celsius? "))
            #kalla í fallið celsius_kelvin til að reikna
            hiti_k = celsius_kelvin(hiti_C)
            print(str(hiti_C) + "°C er " + str(hiti_k) + "°K")
        elif svar == "B":
            hiti_k = float(input("Hvað er hitinn í Kelvin? "))
            #kalla í fallið kelvin_celsius til að reikna
            hiti_C = kelvin_celsius(hiti_k)
            print(str(hiti_k) + "°K er " + str(hiti_C) + "°C")

    elif valm == "3":
        print("Þú hefur valið lið 3")

        grunnTala = float(input("Hver er grunntalan? "))
        veldis = float(input("Í hvaða veldi er talan? "))

        print(grunn_veldi(grunnTala, veldis))

    elif valm == "4":
        print("Þú hefur valið lið 4")

        svar = input("Veldu A ef þú villt breyta tommum í sentimetra\neða B ef þú villt breyta sentimetrum í tommur ").upper()

        if svar == "A":
            tommur = float(input("Hversu margar tommur? "))
            #kalla í tommur_sentimetra til að reikna
            sentiStaerd = tommur_sentimetrar(tommur)
            print(tommur, "tommur eru", round(sentiStaerd, 2), "sentimetrar")
        elif svar == "B":
            sentim = float(input("Hversu margir sentimetrar? "))
            #kalla i sentimetra_tommur til að reikna
            tomStaerd = sentimetra_tommur(sentim)
            print(sentim, "sentimetrar eru", round(tomStaerd, 2), "tommur")

    elif valm == "5":
        print("Þú hefur valið lið 5")

        svar = input("Veldu A ef þú villt breyta gallon í lítra\neða B ef þú villt breyta lítrum í gallon ").upper()

        if svar == "A":
            gallon = float(input("Hversu marga gallon ertu með? "))
            #kalla í gallon_litra til að reikna
            litrar = gallon_litra(gallon)
            print(gallon, "gallon eru", round(litrar), "lítrar")
        elif svar == "B":
            litrar = float(input("Hversu marga lítrar ertu með? "))
            #kalla í litra_gallon til að reikna
            gallon = litra_gallon(litrar)
            print(litrar, "lítrar eru", round(gallon), "gallon")

    elif valm == "6":
        print("Þú hefur valið lið 6")

        svar = input("Hvert er nafn þitt? ")
        kynSvar = input("Ertu kk eða kvk? ").upper()#tekur inputtið sem stórir stafir

        print(nafn_kyn(svar, kynSvar))#birtir nafn_kyn fallið með svar sem nafn og kynSvar sem kyn

    elif valm == "7":
        print("Þú hefur valið lið 7")

        print(kasta()) #birtir fallið kasta

    elif valm == "8":
        print("Þú hefur valið dæmi 8")

        listi1 = []
        listi2 = []

        lengd1 = int(input("Hversu langir eru listarnir? "))

        for x in range(lengd1):#keyrir einsoft og notandi vildi
            svar1 = int(input("Sláðu inn tölu: "))
            listi1.append(svar1)#bætir tölunni í listann
        print("------------")
        for x in range(lengd1):#keyrir einsoft og notandi vildi
            svar2 = int(input("Sláðu inn tölu: "))
            listi2.append(svar2)#bætir tölunni í listann

        print(listi1)#til að sjá listi1
        print(listi2)#til að sjá listi2

        print(thridjiListinn(listi1, listi2))#birtir thridjilistinn með listi1 sem list1 og listi2 sem list2
