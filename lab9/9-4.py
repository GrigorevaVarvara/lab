from PIL import Image
watermark = Image.open("lab9/watermark.png")
img_watermark = Image.open("lab9/cat.jpg")
img_watermark.paste(watermark,(300,100),watermark)
img_watermark.save("lab9/cat_withmark.png")