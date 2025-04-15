import os
from PIL import Image

os.mkdir("lab9/pictures")

for i in range(1, 6):
    filename = str(i)+".jpg"
    image = Image.open(filename)
    image_new = image.convert("L")
    newfilename = "lab9/pictures/"+str(i)+".jpg"
    image_new.save(newfilename)