#Ingvar Vigfússon
#5.9.2017
#föll functions
from random import *

def snorri():#prentar út þrjár setningar
    print("Þetta er sýnidæmi um fall(functions)")
    print("Það er ekki með neina færibreytu")
    print("Það prentar þessar línur á skjáinn")
def konni(skilabod):#birtir þrjár setningar og skilabod
    print("Fall með eina færibreytu, sem heitir skilabod")
    print("skilabod er breyta sem fær gildi þegar kallað er í fallið")
    print("Fallið framkvæmir þær aðgerðir sem eru í því þegar kallað er í það")
    print(skilabod)

def minnstaTala(tala1, tala2, tala3):
    minnsta = 0
    if tala1 <= tala2 and tala1 <= tala3:
        minnsta = tala1
    elif tala2 <= tala3 and tala2 <= tala1:
        minnsta = tala2
    else:
        minnsta = tala3
    return minnsta

def listi_summa(tolur):
    summa=0
    for tala in tolur:
        summa+=tala #bætir tölunni við summa
    return summa


#kalla í föllin
snorri() #kalla í fallið snorri sem hefur enga færibreytu
print("snorri er búinn að prenta línurnar og skila stjórninni tilbaka")
print("-------------------")
# konni() þetta er ekki hægt vegna þess að það vantar færibreytu
konni("ég kallaði í fallið")
print("-------------------")
skilabod = "halló konni"
konni(skilabod)
print("-------------------")
setning = input("Hvað villtu segja við konna? ")
konni(setning)
print("-------------------")
print("minnsta talan er:", minnstaTala(1, 2, 3))
print("-------------------")
tala11 = int(input("Sláðu inn tölu 1 af 3 "))
tala22 = int(input("Sláðu inn tölu 2 af 3 "))
tala33 = int(input("Sláðu inn tölu 3 af 3 "))
print("minnsta talan er:", minnstaTala(tala11, tala22, tala33))
print("-------------------")
listi = []
for i in range(7):
    listi.append(randint(1, 9))
print(listi) #prenta listann til að sjá hvaða tölur eru í honum
print("Summa talnana í listanum er:", listi_summa(listi))
print("-------------------")
#set fallið hér til að ekki þurfa að scrolla upp, má en er gerir forritið ólæsilegra
def setning(nafn='konni',action='sefur',hlutur='rólega'): # hver færibreyta með sjálfgefið gildi
    texti = nafn + " " + action + " " + hlutur
    return texti
#og kalla strax hérna í fallið
setning()
print(setning(hlutur="lengi"))
notandi = input("Hvað heitir þú? ")
athofn = input("Hvað gerir þú? ")
lysing = input("Hvernig gerir þú það? ")
print(setning(nafn=notandi, hlutur=lysing))













