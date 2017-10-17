#17.10.2017
#Ingvar Vigfússon
#Skrifa í skrá python

f = open("test.txt", 'w', encoding= 'utf-8')
f.write("Þetta er fyrsta línan í skránni\n")
f.close()#lokar skrá

try:
    f = open("test.txt", encoding= 'utf-8')
    #opnar test.txt
finally:
    f.close()#lokar skrá

with open("test.txt", 'w', encoding= 'utf-8') as f:
    f.write("This is my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")

with open("test.txt", 'a', encoding= 'utf-8') as f:
    f.write("konráð")
    f.write("\nGuðmundsson")
    f.write("\n Hraunbraut 27")

with open("text.txt", 'w', encoding= 'utf-8') as e:
    e.write("bætum þessari línu líka\n")
with open("text.txt", 'r', encoding= 'utf-8') as e:
    print(e.read(4))
    print(e.read(4))
    print("Nú er teljarinn tilbúinn við staf númer", e.tell())
    print(e.readline())
    e.seek(0)
    for line in e:
        print(line, end="")
    e.seek(0)
    print(e.readlines())

linulisti = []
with open("test.txt", 'r', encoding= 'utf-8') as f:
    linulisti = f.readlines()

print(linulisti)
for x in linulisti:
    print(x[3])