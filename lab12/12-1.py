import json
with open("lab12/data.json", "r", encoding='utf-8') as read_file:
    rf = json.load(read_file)
    for items in rf["products"]:
        name = items['name']
        price = items['price']
        weight = items['weight']
        if items['available'] == True:
            available = "В наличии"
        else: available = "Нет в наличии"

        print(f"Название: {name}")
        print(f"Цена: {price}")
        print(f"Вес: {weight}")
        print(available)
        print("")