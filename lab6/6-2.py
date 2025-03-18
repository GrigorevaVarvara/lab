def divideby100():
    try:
        c = float(input("введите число: "))
        d = 100 / c
        print(f"результат: {d}")
    except ValueError:
        print("ошибка: введите корректное число.")
    except ZeroDivisionError:
        print("ошибка: деление на ноль невозможно.")

divideby100()