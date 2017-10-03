#3.10.2017
#Ingvar Vigfússon
#Skilaverkefni 3

#imports
import random

#valmynd
valm=""
while valm !="4":
    print("\n--------------")
    print("1. Tuples Herrar og dömur")
    print("2. Dæmi")
    print("3. Dæmi")
    print("4. Hætta")
    print("--------------")
    valm=input("")

    if valm == "1":
        print("Þú hefur valið 1. Tuples Herrar og dömur")

        randomPar1 = []
        randomPar = []
        randomParT = []
        randomParC = []
        stafaListi = []
        ollnofn = []
        herraTupla = ('Konráð', 'Snorri', 'Pálmar', 'Magnús', 'Bergsteinn', 'Jón')
        #                0          1         2         3           4         5
        domurTupla = ('Helga', 'Kristborg', 'María', 'Rósa', 'Sofía', 'Anita')
        #                0          1          2        3       4         5
        # Sýnið sitthvort tuplið, nöfnin með bili á milli.
        print("Herra túplan:")
        for x in herraTupla:#keyrir í gegnum herraTupla sem x
            print(x, end=' ')#birtir x með bil á milli
        print("\nDömu túplan:")
        for x in domurTupla:#keyrir í gegnum domurTupla sem x
            print(x, end=' ')#birtir x með bil á milli
        print("\n-----------")
        # Parið saman tuplin þannig að fyrsti herrann dansar við fyrstu dömuna
        for x, y in zip(herraTupla, domurTupla):#keyrir í gegnum herraTupla og domurTupla samtímis
            print(x, "og", y)#birtir x úr HerraTupla og y úr domurTupla

        #eitt random par
        print("\nRandom par:")
        herrar = random.choice(herraTupla)#breyta sem velur random stak úr herraTupla
        domur = random.choice(domurTupla)#breyta sem velur random stak úr domurTupla
        par = (herrar, "og", domur)#breyta sem heldur utan um parið
        if par not in randomPar1:#ef parið er ekki núþegar í randomPar1
            randomPar1.append(par)#bætir parinu við listann
        for x in randomPar1:#keyrir í gegnum randomPar1 sem x
            for stak in x:#fyrir hvert stak í x (Þarf að nota þetta því ég setti tuple í lista
                print(stak, end=" ")#birtir stak með bil á milli

        #öll pörin
        print("\n\nÖll pörin random:")
        while len(randomPar) < len(herraTupla):#á meðan það eru færri stök í randomPar heldur en herraTupla
            herrar = random.choice(herraTupla)#breyta sem velur random stak úr herraTupla
            domur = random.choice(domurTupla)#breyta sem velur random stak úr domurTupla
            par = (herrar, "og", domur)#breyta sem heldur utan um parið
            if par not in randomPar and herrar not in randomParT and domur not in randomParC:
            #checkar ef par er núþegar í randomPar og hvort herrar er núþegar í randomParT og hvort domur er núþegar í randomParC
                randomPar.append(par)#ef já bættu við par í randomPar
                randomParT.append(herrar)#og herrar í randomParT
                randomParC.append(domur)#og domur í randomParC
        for x in randomPar:#keyrir í gegnum randomPar sem x
            print()#birtir bil á milli hvert par, birtir líka bil á milli "Öll pörin random:" og listann
            for stak in x:#fyrir hvert stak í x, notað útaf tuple inní lista
                print(stak, end=" ")#birtir hvert stak með bil á milli

        # Biðjið notandann um að slá inn staf og finnið öll nöfnin sem hafa viðkomandi staf
        print("\n-------")
        stafur = input("Hver er stafurinn? ")#fær staf frá notanda
        for x in herraTupla:#keyrir í gegnum herraTupla sem x
            if stafur in x or stafur.upper() in x:# ef stafur er í x, upper() til að tjékka hástafi
                stafaListi.append(x)#bætir x við stafaListi
        for x in domurTupla:#keyrir í gegnum domurTupla sem x
            if stafur in x or stafur.upper() in x:#ef stafur er í x, upper() til að tjékka hástafi
                stafaListi.append(x)#bætir x við stafaListi
        print("Hér er listi yfir öllum nöfnum með", stafur, "í nafninu")
        for x in stafaListi:#keyrir í gegnum stafaListi sem x
            print(x)#birtir x

        # Finnið bara nöfnin sem hefur viðkomandi staf sem fyrsta staf.
        print("\nHér er listi yfir öllum nöfnum sem byrja á", stafur)
        for x in stafaListi:#keyrir í gegnum stafaListi sem x
            if x[0] == stafur or x[0] == stafur.upper():#ef fyrsti stafurinn í x er sá sami og notanda gaf
                print(x)#birtir x

        # Finnið öll nöfn sem hafa fleiri en eitt n í nafninu
        print("\n-------------")
        for x in herraTupla:
            ollnofn.append(x)
        for x in domurTupla:
            ollnofn.append(x)

        test1 = []
        teljari = 0
        for x in ollnofn:
            for stak in x:
                if stak == "n":
                    teljari += 1
                    if teljari > 1:
                        test1.append(x)
        print(test1)










