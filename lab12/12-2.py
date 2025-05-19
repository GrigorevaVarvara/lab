import json

newitem = input("Хотите добавить новую запись?(да/нет)").lower()
with open("lab12/data.json", "r", encoding='utf-8') as read_file:
    rf = json.load(read_file)

    if (newitem=="да"):
        data = {
            "name": input("Введите название:"),
            "price": int(input("Введите цену:")),
            "weight": int(input("Введите вес:")),
            "available": bool(input("Введите наличние(true/false):"))
        }
        rf["products"].append(data)
        with open("lab12/data.json", "w", encoding='utf-8') as write_file:
            json.dump(rf, write_file, ensure_ascii=False, indent=4)
    
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
    