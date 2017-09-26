#26.9.2017
#Ingvar Vigfússon
#Tuples

my_tuple = ()
print(my_tuple)

my_tuple = (1, 2, 3)
print(my_tuple)

my_tuple = (1, "Hello", 3.4)
print(my_tuple)

my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

my_tuple = 3, 4.6, "dog"
print(my_tuple)

for x in my_tuple:
    print(x, end=' ')

print("\n-----------")

my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_tuple[0])
print(my_tuple[5])

for x in my_tuple:
    print(x, end=' ')
#eða
print()
for x in range(len(my_tuple)):
    print(my_tuple[x], end=' ')
print("\n---")
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
#             0         1           2
#           01234    0  1   2   0  1  2
print(n_tuple[0][3])
print(n_tuple[1][1])
print("---")
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_tuple[-1])
print(my_tuple[-6])
print("---")
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple[1:4])#stök frá 1 upp að 4(ekki 4)
print(my_tuple[:-7])#stak 7 aftan frá og til enda
print(my_tuple[7:])#Stak 7 framanfrá og til enda
print(my_tuple[:])#frá byrjun til enda
print("---")
tuple_1 = (1, 2, 3)
tuple_2 = (4, 5, 6)
print(tuple_1 + tuple_2)
tuple_3 = ("Repeat", "endurtaka")
print(tuple_3 * 3)
print("---")
my_tuple = ('a', 'p', 'p', 'l', 'e',)
print(my_tuple.count('p'))#telur fjölda p, s.s. 2
print(my_tuple.index('l'))#segir hvar stafurinn er í tuple s.s. nr 3
print("---")
my_tuple = ('a', 'p', 'p', 'l', 'e',)
print('a' in my_tuple)#ef a í tuple: True
print('b' in my_tuple)#utskrift: False
print('g' not in my_tuple)#ef g ekki í tuple: utskrift True