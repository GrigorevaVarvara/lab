from PIL import Image
from pathlib import Path
import os

fpath = Path("lab11/pictures")
filetype = (".png", ".jpg")

for file_path in fpath.iterdir():
    file_rashirenie = file_path.suffix.lower()
    if file_rashirenie in filetype:
        filename = "lab11/pictures/" + file_path.name
        image = Image.open(filename)
        image.show()
        print(f"Размер:{image.size}")
        print(f"Формат: {image.format}")
        print(f"Цветовая модель: {image.mode}")
