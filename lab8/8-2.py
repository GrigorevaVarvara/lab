one_point={"А", "В", "Е", "И", "Н", "О", "Р", "С", 'Т'}
two_point={"Д", "К", "Л", "М", "П", "У"}
three_point={"Б", "Г", "Ё", "Ь", "Я"}
four_point={"Й", "Ы"}
five_point={"Ж", "З", "Х", "Ц", "Ч"}
eight_point={"Ш", "Э", "Ю"}
ten_point={"Ф", "Щ", "Ъ"}

word = input("введите слово: ").upper()
score=0
for letter in word:
    if letter in one_point:
        score +=1
    elif letter in two_point:
        score+=2
    elif letter in three_point:
        score+=3
    elif letter in four_point:
        score+=4
    elif letter in five_point:
        score+=5
    elif letter in eight_point:
        score+=8
    elif letter in ten_point:
        score+=10
    else:
        print("ой что то пошло не так")
        break
print("ваш счет: ",score)