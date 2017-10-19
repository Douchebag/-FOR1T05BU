#17.10.2017
#Ingvar Vigfússon
#Skilaverkefni 4
import random

#1
with open("slettartolur.txt", 'w', encoding='utf8') as f:
    for i in range(2, 1001, 2):
        f.write(str(i)+" ")

#a.	Lesið skránna og setjið lista. Prentið út listann
listi = []
with open("slettartolur.txt", 'r', encoding='utf-8') as f:
    listi = f.readlines()
print(listi)

#b.	Finnið summu og meðaltal talnanna með tveimur aukastöfum
listi = []
with open("slettartolur.txt", 'r', encoding='utf-8') as f:
    line = f.read()
    line.strip()
    listi = (line.split(' '))
listi.remove('')
listi = list(map(int, listi))

print("Summa listans er:", sum(listi))
print("Meðaltal listans er:", (format((sum(listi)/len(listi)), "0.2f")))

#c.	Hendið öllum tölum sem 8 gengur upp í og setjið í aðra skrá (sumarslettartolur.txt)

with open("sumarslettartolur.txt", 'w', encoding='utf-8') as e:
    for x in listi:
        if x % 8 == 0:
            e.write(str(x) + ' ')

#d.	Prentið út skrána með bil milli talna og 10 tölur í línu
teljari = 0

with open("sumarslettartolur.txt", 'r', encoding='utf-8') as e:
    for x in listi:
        teljari += 1
        print(x, end=" ")
        if teljari == 10:
            print("")
            teljari = 0

#2.	Búið til skrá sem innheldur  fyrstu 100 prímtölurnar. Setjið tölurnar inn með því að nota for slaufur.

#a.	Prentið út skránna
with open("primetolur.txt", 'w', encoding='utf8') as f:
    for i in range(2, 101):
        if i == 0 or i == 1:
            break
        for x in range(2, i):
            if i % x == 0:
                break
        else:
            f.write(str(i) + " ")

#b.	Prentið allar tölur sem innhalda 7
primlisti = []
with open("primetolur.txt", 'r', encoding='utf-8') as f:
    line = f.read()
    line.strip()
    primlisti = (line.split(' '))
primlisti.remove('')
primlisti = list(map(int, primlisti))
for x in primlisti:
    if "7" in str(x):
        print(x, end=" ")

#c.	Prentið  svo  út fjórðu hverja tölu og setjið inn í aðra skrá. Prentið þá skrá út.
with open("fjordaprime.txt", 'w', encoding='utf8') as f:
    teljari = 0
    for x in primlisti:
        teljari += 1
        if teljari == 4:
            f.write(str(x) + " ")
            teljari = 0
print("")

#3.	Hannið forrit sem hefur að geyma þrjár tuples.
with open("tuplur.txt", 'w', encoding='utf8') as f:
    tupla1 = []
    for x in range(1, 10):
        tupla1.append(x)
    f.write(str(tuple(tupla1)) + "\n")

    stafir = "abcdefghijklmnopqrstuvwxyz"
    tupla2 = []

    for x in range(1, 9):
        tupla2.append(random.choice(stafir))
    f.write(str(tuple(tupla2)) + "\n")

    tupla3 = ("konni", 123, "sponni", 234)
    f.write(str(tupla3) + "\n")

#a.	Prentið út hverja tuple fyrir sig
with open("tuplur.txt", 'r', encoding='utf-8') as f:
    for x in f:
        print(x, end="")

#b.	Bætið inn við tupplu
tupla = []
with open("tuplur.txt", 'r', encoding='utf-8') as f:
    line = f.readline()
    line.strip()
    tupla = (line.split('\n'))
    #tupla.remove('(')
    for i in f.readline():
        tmp = i.split(", ")
        try:
            tupla.append(tmp)
        finally:
            f.close()
print(tupla)


#4
'''
f.write("dictionar harð kóðað bara")
notað eval
'''








