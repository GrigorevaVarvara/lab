from random import randint

numbers = [randint(1, 100) for x in range(5)]
a=int(input("Введите число"))
print(numbers)
print('Ваше число - ',a)
if (a in numbers) == True:
    print('ура ура вы угадали молодец!!!')
else:
    print('блинб не угадали может в следующий раз(((')
