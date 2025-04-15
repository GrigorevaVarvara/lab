from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

holidays={"1":"День жаренных гвоздей","2":"День глазированного сырка","3":"День ватрушки"}
for key in holidays:
    print(key, " - ", holidays[key])

n = input("выберите праздник и напишите номер: ")
name = input("кого вы хотите поздравить: ")

if n in holidays:
    filename = "lab10/postcards/"+n+".jpg"
    card = Image.open(filename)
    card_new = ImageDraw.Draw(card)
    font = ImageFont.truetype("arial.ttf", 50)
    message = name + ", поздравляю!"
    if n == "1":
        position = (300, 200)
        fill_color = (53, 50, 201)
    elif n == "2":
        position = (600, 200)
        fill_color = (235, 47, 103)
    else:
        position = (200, 800)
        fill_color = (0, 0, 0)
    card_new.text(position, message, font=font, stroke_width=2, fill=fill_color)
    card.show()
    card.save('lab10/named/'+name+".png")
else: 
    print("ну видимо сегодня не празднуем")