#28.9.2017
#Ingvar Vigfússon
#Python Dictionary

my_dict = {'nafn': 'Ingvar', 'aldur': 18}
print(my_dict)
print(my_dict['nafn'])
print(my_dict['aldur'])
#ekki hægt, færð key error print(my_dict['haed'])

#að prenta út key og value pör línu fyrir línu
my_dict = {1: 'apple', 2: 'ball', 3: 'orange', 4: 'banana'}
for x in my_dict:
    print(x, "\t", my_dict[x])#x stendur fyrir lyklana my_dict[x] er value-ið í my_dict sem er á móti x
#eða svona
for key, value in my_dict.items():#tekur pörin beint
    print("%i -> %s" % (key, value))#% sem placeholder og i fyrir integer og s fyrir string
#                      Þarf að vera í réttri röð
#en önnur leið
for key, value in my_dict.items():
    print("{0} er {1} er með lykli {0}" .format(key, value))
#                                   ^möguleiki á að nota sama tvisvar án þess að setja annað í key,value

#Það er hægt að breyta og bæti inn í dictionary
my_dict = {'nafn': 'Ingvar', 'aldur': 18}
my_dict['aldur'] = 19
print(my_dict)
my_dict['heimilisfang'] = 'hraunbaer 4'
print(my_dict)
#og eyða eða fjarlægja
print(my_dict.popitem())#fjarlægjir random pari og birtir það
print(my_dict)


