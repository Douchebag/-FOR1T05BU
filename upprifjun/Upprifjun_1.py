#22.8.2017
#Ingvar Vigfússon
#Upprifjun 1

#Valmynd
valm=""
while valm !="7":
    print("\n--------------")
    print("Dæmi. 1")
    print("Dæmi. 2")
    print("Dæmi. 3")
    print("Dæmi. 4")
    print("Dæmi. 5")
    print("Dæmi. 6")
    print("Hætta. 7")
    print("--------------")
    valm=input("")

    #Dæmi 1
    if valm == "1":
        print("Þú hefur valið dæmi. 1 ")
        print("Sláðu inn tvær tölur sem verða síðan lagðar og margfaldaðar")
        tala1=int(input("Sláðu inn fyrstu töluna hér "))
        tala2=int(input("Sláðu inn seinni töluna hér "))
        margf=tala1 * tala2
        samanleg=tala1 + tala2
        print("Tölurnar lagðar saman eru:", margf)
        print("Tölurnar margfaldaðar saman eru:", samanleg)

    if valm == "2":
        print("Þú hefur valið dæmi. 2")
        print("Sláðu inn fornafn og eftirnafn")

        forn=input("Hvert er fornafn þitt? ")
        eftirn=input("Hvert er eftirnafn þitt? ")

        print("Sæl/l", forn, eftirn)

    if valm == "3":
        print("Þú hefur valið dæmi. 3")
        print("Sláðu inn lengd í kílómetrum, birtir forritið lengina í metrum")

        kilospurn=float(input("Sláðu inn lengd í kílómetrum "))

        metrar=kilospurn * 1000

        print(kilospurn, "kílómetrar eru", metrar, "metrar")

    if valm == "4":
        print("Þú hefur valið dæmi. 4")
        print("Sláðu inn laun á klukkustund og fjölda klukkustunda")

        laun=int(input("Hversu mikið færðu borgar á klukkustund? "))
        klst=int(input("Hversu margar klukkustundir vinnur þú? "))

        margf=laun * klst

        print("Heildarlaun þín eru:", margf, "krónur")

    if valm == "5":
        print("Þú hefur valið dæmi. 5")
        print("Sláðu inn laun á klukkustund og fjölda klukkustunda")

        laun = int(input("Hversu mikið færðu borgar á klukkustund? "))
        klst = int(input("Hversu margar klukkustundir vinnur þú? "))

        margf = laun * klst

        if margf > 30000:
            skattur=margf * 0.2
            print("Heildarlaun þín eru:", margf, "krónur")
            print("Skattur:", skattur, "krónur")

    if valm == "6":
        print("Þú hefur valið dæmi. 6")
        print("Sláðu inn fjölda gráða")

        gradur=int(input("Hversu margar gráður? "))
        deil= gradur // 360
        modulo = gradur % 360
        print("Það eru", deil, "hringir og", modulo, "gráður")



















