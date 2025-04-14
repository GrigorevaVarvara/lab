countries={"Нидерланды":"Амстердам","Греция":"Афины","Германия":"Берлин","Швейцария":"Берн"}
for key in countries:
    print(key, " - ", countries[key])

n = input("введите страну: ")

if n in countries:
    group = countries[n]
    print("столица - ",group)
else:
    print("такой страны пока не знаем")

list_keys = list(countries.keys()) 
list_keys.sort()
for i in list_keys:
    print(i, ':', countries[i])