word=input("Введите слово: ")

for c in word:
    if c.lower() == "ф":
        print("Ого! Это редкое слово!")
        break
else:
    print("Эх, это не очень редкое слово...")