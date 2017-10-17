#17.10.2017
#Ingvar Vigfússon
#Skilaverkefni 4

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

with open("sumarslettartolur.txt", 'r', encoding='utf-8') as e:
