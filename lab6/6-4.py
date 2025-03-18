def luckyticket():
    number = input("номер билета: ")
    if len(number)%2!=0:
        raise ValueError("неправильный номер")
    half = len(number) // 2
    half1 = sum(map(int, number[:half]))
    half2 = sum(map(int, number[half:]))
    if half1==half2:
        print("счастливый билетик!!")
    else:
        print("в другой раз повезет")






luckyticket()