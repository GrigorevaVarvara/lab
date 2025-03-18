import random

errors = 0
answers = 0

while errors < 3:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = int(input(f"{a} + {b} = "))
    if c==a+b:
        answers+=1
        print("правильно!!")
    else:
        errors+=1
        print("неправильно >:(")

print(f"Игра окончена. Правильных ответов: {answers}")