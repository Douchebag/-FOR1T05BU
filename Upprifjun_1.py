#22.8.2017
#Ingvar Vigfússon
#Upprifjun 1

#Valmynd
valm=""
while valm !="7":
    print("\n\n--------------")
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
