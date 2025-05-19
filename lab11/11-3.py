import csv
file = open('lab11/data.csv', encoding='utf-8')
sum = 0
shopping_list=[]
reader = csv.DictReader(file)

for row in reader:
    product = row["Продукт"]
    number= int(row["Количество"])
    price = int(row["Цена"])
    cost = price*number
    sum += cost
    shopping_list.append(f"{product} - {number} шт. за {price} руб.")

print("Нужно купить:")
for i in shopping_list:
    print(i)
print(f"Итоговая сумма: {sum} руб.")