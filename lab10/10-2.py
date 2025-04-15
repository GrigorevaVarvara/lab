from PIL import Image

holidays={"1":"День жаренных гвоздей","2":"День глазированного сырка","3":"День ватрушки"}
for key in holidays:
    print(key, " - ", holidays[key])

n = input("выберите праздник и напишите номер: ")

if n in holidays:
    filename = "lab10/postcards/"+n+".jpg"
    card = Image.open(filename)
    card.show()
else: 
    print("ну видимо сегондня не празднуем")