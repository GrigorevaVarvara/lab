b=""

while True:
    word=input("Введите слово или stop: ")
    if word.lower() == "stop":
        break
    b = b + " " + word
print(b)