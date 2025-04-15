from PIL import Image
image = Image.open("lab9/cat.jpg")
image.show()

print(f"Размер:{image.size}")
print(f"Формат: {image.format}")
print(f"Цветовая модель: {image.mode}")