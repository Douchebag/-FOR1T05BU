#Ingvar Vigfússon
#5.9.2017
#föll functions

def snorri():
    print("Þetta er sýnidæmi um fall(functions)")
    print("Það er ekki með neina færibreytu")
    print("Það prentar þessar línur á skjáinn")
def konni(skilabod):
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