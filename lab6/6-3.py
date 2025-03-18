def magicaldate():
    day = int(input("введите день от 1 до 31: "))
    month = int(input("введите месяц от 1 до 12: "))
    year = int(input("введите год: "))
    if (day<1)or(day>31):
        raise ValueError("день должен быть от 1 до 31")
    if (month<1)or(month>12):
        raise ValueError("месяц должен быть от 1 до 12")
    if (year%100)==(day*month):
        print ("дата магическая!!")
    else:
        print ("дата не магическая!!")


magicaldate()
