#7.9.2017
#Ingvar Vigfússon
#föll æfingaverkefni 3

#föll

def skrifaUt(listi):
    print(listi)

def staersta(listi):
    staersta = listi[0]
    for num in listi:
        if staersta < num:
            staersta = num
    return staersta

def minnsta(listi):
    minnsta = listi[0]
    for num in listi:
        if minnsta > num:
            minnsta = num
    return minnsta

def summa(listi):
    summa = 0
    for x in listi:
        summa += x
    return summa

#forrit

listi = []
for x in range(5):
    tala = int(input("Sláðu inn tölu "))
    listi.append(tala)

skrifaUt(listi) #birta lista

print(staersta(listi)) #birtir stærstu töluna

print(minnsta(listi)) #birtir minnstu töluna

print(summa(listi)) #birtir summu listans