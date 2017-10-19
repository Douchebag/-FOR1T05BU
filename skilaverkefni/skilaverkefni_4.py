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
print("---------------")
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
print("---------------")

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
print("---------------")

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
print("\n---------------")
#c.	Prentið  svo  út fjórðu hverja tölu og setjið inn í aðra skrá. Prentið þá skrá út.
with open("fjordaprime.txt", 'w', encoding='utf8') as f:
    teljari = 0
    for x in primlisti:
        teljari += 1
        if teljari == 4:
            f.write(str(x) + " ")
            teljari = 0
            print(x)


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
print("----")
#a.	Prentið út hverja tuple fyrir sig
with open("tuplur.txt", 'r', encoding='utf-8') as f:
    for x in f:
        print(x, end="")


#b.	Bætið inn við tupplu
tupla = []
fyrsta = []

with open("tuplur.txt", 'r', encoding='utf-8') as f:

    line = f.read()
    line.strip()
    tupla = (line.split('\n'))
    tupla.remove('')


test = list(tupla[0])

test.insert(26, ',')
test.insert(27, ' ')
test.insert(28, '10')

test2 = []
tolur = '12345678910'

for x in test:
    if x in tolur:
        test2.append(x)

newdata = line.replace(str(tuple(tupla1)),str(tuple(test2)))

with open('tuplur.txt', 'w', encoding='utf-8') as f:
    f.write(newdata)

#c.	Finnið summu fyrstu tupplunar.
test2 = list(test2)
summa = 0

for x in test2:
    summa += int(x)
medaltal = summa/len(test2)
print("----")
print("Summa tupplunar er:", summa)
print("Meðaltal tupplunar er:", round(medaltal, 2))

#4.	Hannið forrit sem býr til skrá sem geymir dictionary.

#a og b
with open("dictionary.txt", 'w', encoding='utf8') as f:
    f.write("{'konni': 1, 'snorri': 2, 'kalli': 3, 'palli': 4}\n")

#c.	Bætið við tveimur dictionarys
dic1 = {1: 'gulur', 2: 'bleikur', 3: 'rauður'}
dic2 = {'einn': 1, 'tveir': 2, 'thrir': 3, 'fjorir': 4, 'fimm': 5}
with open("dictionary.txt", 'a', encoding='utf8') as f:
    f.write(str(dic1) + "\n")
    f.write(str(dic2) + "\n")

#d.	Prentið út dictionaryin eitt í einu. Eitt  sett(key,value) í sér línu.
dict = {}
with open("dictionary.txt", 'r', encoding='utf8') as f:
    line = f.read()
    line.strip()
    dict = (line.split('\n'))
    dict.remove('')

dict1 = eval(dict[0])
dict2 = eval(dict[1])
dict3 = eval(dict[2])
print("----")
for key, value in dict1.items():
    print("{0}:{1}" .format(key, value))
print("")
for key, value in dict2.items():
    print("{0}:{1}" .format(key, value))
print("")
for key, value in dict3.items():
    print("{0}:{1}" .format(key, value))