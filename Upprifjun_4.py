#24.8.2017
#Ingvar Vigfússon
#Upprifjun 4

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
        print("Sláðu inn setningu hér fyrir neðan")
        setning = input("")

        teljari = 0
        for x in setning:
            if x == "n":
                teljari += 1
        print("það eru", teljari, "n í þessari setningu")










