#7.9.2017
#Ingvar Vigfússon
#föll æfingaverkefni 2

#föll
def reiknaRummalKulu(radius):
    rummalKulu = (4.0 * 3.14 * (radius * radius* radius)) / 3.0
    return rummalKulu

def reiknaRummalKassa(lengd, breidd, haed):
    rummalKassa = lengd * breidd * haed
    return rummalKassa

def reiknaFlatarmalThrihyrnings(breidd, haed):
    flatarmalThri = (breidd * haed) / 2
    return flatarmalThri

#valmynd
valm=""
while valm !="4":
    print("\n--------------")
    print("1. Rúmmál kúlu")
    print("2. Rúmmál kassa")
    print("3. Flatarmál þríhyrnings")
    print("4. Hætta")
    print("--------------")
    valm=input("")

    if valm == "1":
        radius = int(input("Hver er radius hringsins? "))
        print(reiknaRummalKulu(radius))

    elif valm == "2":
        lengd = int(input("Hver er lengd þríhyrningsins? "))
        breidd = int(input("Hver er breidd þríhyrningsins? "))
        haed = int(input("Hver er haed þríhyrningsins? "))

        print(reiknaRummalKassa(lengd, breidd, haed))

    elif valm == "3":
        breidd = int(input("Hver er breidd þríhyrningsins "))
        haed = int(input("Hver er haed þríhyrningsins "))

        print(reiknaFlatarmalThrihyrnings(breidd, haed))

    elif valm == "4":
        print("Þú hefur valið að hætta")

    else:
        print("Villa, skrifaðu rétta tölu")






