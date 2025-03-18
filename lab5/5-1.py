a=int(input("Введите количество слов: "))
b=""

for i in range(a):
    word=input("Введите слово: ")
    b = b + " " + word
print(b)