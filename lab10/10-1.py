from PIL import Image
image = Image.open('lab10/image.png')
cropped = image.crop((100, 0, 735, 170))
cropped.save('lab10/cropped_image.png')