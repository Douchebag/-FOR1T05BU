#28.9.2017
#Ingvar Vigfússon
#Æfingaverkefni fyrir dictionary

#1. Hannið dictionary sem innheldur 10 stök með númer sem key og liti value.
litir = {1: 'gulur', 2: 'bleikur', 3: 'rauður', 4: 'svartur', 5: 'hvítur', 6: 'appelsínugulur', 7: 'græn', 8: 'blár', 9: 'fjólublár', 10: 'brúnn'}
#2.	Skrifið út dictionaryið í dæmi 1 þannig að hvert númer og litur er í einni línu
for key, value in litir.items():
    print("númer %i er %s" % (key, value))
#3. Skrifið út lit númer 4. (svartur)
print(litir[4])
#4. Breyttu lit númer 5 í appelsínugult
litir[5] = 'appelsínugult'
#5.	Skrifaðu út  breytt dictionary
print(litir)
#6.	Fjarlægðu lit númer 2
litir.pop(2)
#7.	Skrifaðu út  breytt dictionary
print(litir)
#8.	Notaðu popitem() aðferðina til að henda út random staki
litir.popitem()
#9.	Skrifaðu út  breytt dictionary
print(litir)
#10. Gerðu afrit af dictionaryinu
litir2 = litir
#11. Eyddu öðru dictionaryinu
del litir
#12. Reyndu að skrifa út dictionaryið sem þú eyddir. Hvaða melding kemur
#print(litir)
print("NameError: name 'litir' is not defined")
#13. Búðu til nýtt dictionary með heiltölur sem key frá 1 til og með 5 og eitthvað annað sem values.
nytt_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
#14. Sýndu frá á notkun á eftirfarandi aðferðum tengdar dictionary
for key, value in nytt_dict.items():#tekur pörin beint
    print("{0} sinnum {0} = {1}" .format(key, value))
print("----")
for key in nytt_dict.keys():
    print("%i" % (key))
print("----")
for value in nytt_dict.values():
    print("%i" % (value))
print("----")
print(nytt_dict)
print(nytt_dict.clear())#tæmir og birtir nytt_dict




