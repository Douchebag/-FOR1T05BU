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
    print("2. Símaskrá")
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
        #for x in ollnofn:
            #ekki búið

    elif valm == "2":
        print("Þú hefur valið 2. Símaskrá")

        simakra = {"Konráð": 2325523, "Snorri": 1234233, "Magnús": 5432231, "Sofía": 4326654, "Jón": 8763342, "Anita": 6853355, "Rósa": 7658899, "María": 9874452, "Kristborg": 5347765, "Helga": 5437522}

        svar = input("Hvert er nafnið? ")

        for x in simakra:
            if x == svar:
                print(x, simakra[x])

    elif valm == "3":
        print("Þú hefur valið 3. bekkur")

        teljari = 0

        bekkur = {"Hrannar": 17, "Gudmundur": 18, "Sigurkarl": 17, "Arnsteinn": 16, "Lilja": 17, "Kristlind": 18, "Huginn": 17, "Runar": 18, "Marino": 16, "Johann": 17, "Hafros": 17, "Rut": 18, "Oddfreyja": 17, "Sigurpall": 18, "Gudridur": 17}

        #allir nemendur og aldur
        for x in bekkur:
            print(x, "------", bekkur[x])

        #18+
        print("---------")

        for x in bekkur:
            if bekkur[x] >= 18:
                teljari += 1
                print(x)
        print("Það eru", teljari, "nemendur í þessum bekk sem eru 18+")

        #medalaldur
        print("---------")
        aldurListi = []

        for x in bekkur:
            aldurListi.append(bekkur[x])

        form = sum(aldurListi) / len(aldurListi)
        print("Meðalaldur:", form)

        #heildar aldur

        print("Heildaraldur:", sum(aldurListi))

        #Biður um staf og skrifar út nafn + aldur

        stafur = input("Hvaða staf byrjar nafnið á? ").upper()
        teljari = 0
        aldur = []
        for x in bekkur:
            if x[0] == stafur:
                print(x, bekkur[x])
                teljari += 1
                aldur.append(bekkur[x])
        formula = sum(aldur) / teljari
        print("Meðalaldur þeirra:", formula)
