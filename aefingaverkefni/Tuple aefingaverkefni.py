#26.9.2017
#Ingvar Vigfússon
#Tuples æfingaverkefni

#valmynd
valm=""
while valm !="6":
    print("\n--------------")
    print("1. Dæmi")
    print("2. Dæmi")
    print("3. Dæmi")
    print("4. Dæmi")
    print("5. Dæmi")
    print("6. Hætta")
    print("--------------")
    valm=input("")

    if valm == "1":
        tupla_1 = (1, 'hallo', 'bless', 6, 'test', 'hae', 'bae')
        print("Stak nr.3 er:", tupla_1[2])

        for x in tupla_1:
            print(x, end=":")

    elif valm == "2":
        tupla_2 = (['a', 'c'], [7, 4], [24, 5], ['z', 's', 'd'])
        #               0         1       2             3
        #            0    1     0  1    0   1     0    1    2
        print(tupla_2)
        print(tupla_2[1][1])

    elif valm == "3":
        tupla_3 = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n')
        #           0    1    2    3    4    5    6    7    8    9    10   11   12   13
        print(tupla_3[4])#stak 4 er fimmti stafurinn
        print(tupla_3[-4])#fjórða aftasta stakið
        print(tupla_3[2:9])#frá 2 og upp að 9, tekur ekki 9 með

    elif valm == "4":
        tupla_4 = (1, 2, 3, 4, 5)
        tupla_44 = []

        margfTal = int(input("Hver er margföldunar talan? "))

        for x in tupla_4:
            margf = x * margfTal
            tupla_44.append(margf)
        print(tuple(tupla_44))

    elif valm == "5":
        tuple_a = ('a', 'v', 'c', 'x', 'o', 'y', 'd')

        stafur = input("Hver er stafurinn? ")

        if stafur in tuple_a:
            print("Stafurinn", stafur, "er í tuple_a")
        else:
            print("Stafurinn", stafur, "er ekki í tuple_a")