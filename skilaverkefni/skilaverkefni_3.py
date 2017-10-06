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
    print("3. Bekkur")
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
        for x in herraTupla:#keyrir i gegnum herraTupla sem x
            ollnofn.append(x)#bætir við x í ollnofn
        for x in domurTupla:#keyrir i gegnum domurTupla sem x
            ollnofn.append(x)#bætir við x í ollnofn

        output = []
        teljari = 0

        for nafn in ollnofn:  #keyrir i gegnum ollnofn sem nafn

            for stafur in nafn:  #keyrir i gegnum nafn sem stafur
                if stafur == "n":  #ef stafur er n
                    teljari += 1 #bætir einum við teljarann

            if teljari > 1:  #ef hann er stærri en 1 þá eru 2+ n í nafninu
                output.append(nafn)  #ef svo er þá er nafnið appendað í output

            teljari = 0  # reset-ar teljarann

        print("Nöfnin sem hafa fleiri en eitt n:", output)

    elif valm == "2":
        print("Þú hefur valið 2. Símaskrá")

        simakra = {"Konrad": 2325523, "Snorri": 1234233, "Magnús": 5432231, "Sofía": 4326654, "Jón": 8763342, "Anita": 6853355, "Rósa": 7658899, "María": 9874452, "Kristborg": 5347765, "Helga": 5437522}

        svarU = input("Hvert er nafnið? ")
        svar = svarU[0].upper() + svarU[1:] #Breytir fyrsta stafinum í stórann staf

        for x in simakra:#keyrir i gegnum simaskra sem x. x er þá lykillinn, ekki gildið
            if x == svar:#ef x er sama og svar
                print(x, simakra[x])#birtir x og gildi þess

    elif valm == "3":
        print("Þú hefur valið 3. bekkur")

        teljari = 0

        bekkur = {"Hrannar": 17, "Gudmundur": 18, "Sigurkarl": 17, "Arnsteinn": 16, "Lilja": 17, "Kristlind": 18, "Huginn": 17, "Runar": 18, "Marino": 16, "Johann": 17, "Hafros": 17, "Rut": 18, "Oddfreyja": 17, "Sigurpall": 18, "Gudridur": 17}

        #allir nemendur og aldur
        for x in bekkur:#keyrir í gegnum bekkur sem x
            print(x, "------", bekkur[x])#birtir x(lykill) og gildi x

        #18+
        print("---------\nNemendur sem eru 18+")

        for x in bekkur:#keyrir i gegnum bekkur sem x
            if bekkur[x] >= 18:#ef gildi x er staerri eða jafn 18
                teljari += 1#bætir einum við teljara
                print(x)#birtir x
        print("Það eru", teljari, "nemendur í þessum bekk sem eru 18+")#birtir teljarann

        #medalaldur
        print("---------")
        aldurListi = []

        for x in bekkur:#keyrir í gegnum bekkur sem x
            aldurListi.append(bekkur[x])#bætir gildi x við aldurListi

        form = sum(aldurListi) / len(aldurListi)#tekur summu listans og deilir með fjölda staka í listanum
        print("Meðalaldur:", form)#birtir meðalaldur

        #heildar aldur

        print("Heildaraldur:", sum(aldurListi))#birtir summu listans

        #Biður um staf og skrifar út nafn + aldur

        stafur = input("Hvaða staf byrjar nafnið á? ").upper()#tekur inn staf og breytir í stórann
        teljari = 0
        aldur = []
        for x in bekkur:#keyrir í gegnum bekkur sem x
            if x[0] == stafur:#ef fyrsta stak í x er sama og stafur sem notandi gefur
                print(x, bekkur[x])#birtir x og gildi þess
                teljari += 1#bætir einum við teljara
                aldur.append(bekkur[x])#bætir gildinu við lista aldur
        formula = sum(aldur) / teljari#tekur summu listans og deilir með teljaranum
        print("Meðalaldur þeirra:", formula)#birtir formuluna

    elif valm == "4":#ef valið er 4 stoppar forritið
        break

    else:
        print("Villa. Rangur innsláttur")