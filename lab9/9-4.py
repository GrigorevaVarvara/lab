from PIL import Image
watermark = Image.open("watermark.png")
img_watermark = Image.open("cat.jpg")
img_watermark.paste(watermark,(300,100),watermark)
img_watermark.save("cat_withmark.png")