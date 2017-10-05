#5.10.2017
#Ingvar Vigfusson
#Python sets
'''
my_set = {1, 2, 3}
print(my_set)

my_set = { 1.0, "Hello", (1, 2, 3)}
print(my_set)

my_list = [1, 3, 7, 9]
print(my_list)
my_set = set(my_list)
print(my_set)
my_set.add(5)
print(my_set)
my_set.update([1, 2, 3, 4, 5], {6, 7, 8})
print(my_set)
my_set.discard(10)#keyrir forrit áfram þó að 10 er ekki í set-inu
print(my_set)
my_set.remove(3)#ef talan er ekki í set-inu crashar forritið með KeyError
print(my_set)

#prófum að kasta streng í set

my_set = set("FrábærForritari")
print(my_set)

print(my_set.pop())#birtir hvaða staki er pop-að
print(my_set)

my_set.clear()
print(my_set)
del my_set
# print(my_set) get ekki birt hlut sem er ekki til

#vinnum með tvö set. það er hægt að vera með fleiri

set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}

print(set_A | set_B)#birtir bæð set en hvern stak bara einu sinni

print(set_A & set_B)
#print(set_A.intersection(set_B)) sama og &

print(set_A - set_B)#birtir tölurnar sem eru einstakar í set_A
print(set_B - set_A)#birtir tölurnar sem eru einstakar í set_B
# set_A.difference(set_B) sama og -

print(set_A ^ set_B)
print(set_B.symmetric_difference(set_A))#það sama og ^

set_A.difference_update(set_B)
print(set_A)

# með char

set_A = set("Frábær")
set_B = set("Forritari")

print(set_A | set_B)#birtir bæði set en hvern stak bara einu sinni

print(set_A & set_B)
#print(set_A.intersection(set_B)) sama og &

print(set_A - set_B)#birtir tölurnar sem eru einstakar í set_A
print(set_B - set_A)#birtir tölurnar sem eru einstakar í set_B
# set_A.difference(set_B) sama og -

print(set_A ^ set_B)
print(set_B.symmetric_difference(set_A))#það sama og ^

set_A.difference_update(set_B)
print(set_A)

# með orð

set_A = {"halló", "bless", "dagur"}
set_B = {"bless", "nótt", "velkominn"}

print(set_A | set_B)#birtir bæð set en hvern stak bara einu sinni

print(set_A & set_B)
#print(set_A.intersection(set_B)) sama og &

print(set_A - set_B)#birtir tölurnar sem eru einstakar í set_A
print(set_B - set_A)#birtir tölurnar sem eru einstakar í set_B
# set_A.difference(set_B) sama og -

print(set_A ^ set_B)
print(set_B.symmetric_difference(set_A))#það sama og ^

set_A.difference_update(set_B)
print(set_A)'''

talnasettA = {12,34,4,5,67,89,6,1,77,99,101}
talnasettB = {121,34,4,5,66,89,61,1,76,91,101}

#1.	Skrifið út bæði set-in
print("talnasettA:", talnasettA)
print("talnasettB:", talnasettB)

#2.	Bætið við tölu í talanasettA. Sýnið talnasettið
talnasettA.add(32)
print(talnasettA)

#3.	Takið út tölu í talansettB. Sýnið talnasettið
talnasettB.discard(34)
print(talnasettB)

#4.	Notið pop() aðferðina til að taka út stak í talnasettA. Sýnið talnasettið
talnasettA.pop()
print(talnasettA)

#5.	Sýnið það sem er sameiginlegt með talnasettunum
print(talnasettA & talnasettB)

#6.	Sýnið það sem er ólíkt með talansettunum
print(talnasettA ^ talnasettB)

#7.	Sýnið það sem er bara í talansettA
print(talnasettA - talnasettB)

#8.	Sýnið þau stök sem eru í talansettiA og talnasettiB en ekki í báðum
print(talnasettA.symmetric_difference(talnasettB))

#9.	Sýnið það sem er bara í talansettB
print(talnasettB - talnasettA)