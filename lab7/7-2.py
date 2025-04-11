from random import randint

numbers = [randint(1, 10) for x in range(5)]
repeat = False
for x in numbers:
    if numbers.count(x)>1:
        a=x
        repeat=True
        break

if repeat==True:
    print('повторяется число ', a)
else:
    print('ничего не повторяется')