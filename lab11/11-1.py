import os
from PIL import Image

os.mkdir("lab11/pictures_new")

for i in range(1, 6):
    filename = "lab11/pictures/"+str(i)+".jpg"
    image = Image.open(filename)
    image_new = image.convert("L")
    newfilename = "lab11/pictures_new/"+str(i)+".jpg"
    image_new.save(newfilename)