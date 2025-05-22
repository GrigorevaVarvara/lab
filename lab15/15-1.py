import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageFont
from io import BytesIO

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ветер Перемен")
        self.root.geometry("400x570")
        self.api_key = open("lab15/api_key_1.txt").readline()
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Погодные погоды", font=("Luminari", 32), bg='#EE7878')
        self.title_label.pack(pady=10)
        self.city_label = tk.Label(self.root, text="Введите город:", font=("Luminari", 20), bg='#EE7878')
        self.city_label.pack()
        self.city_entry = tk.Entry(self.root, font=("Luminari", 15), width=30, bg='#FFDCDC')
        self.city_entry.pack(pady=5)
        self.search_button = tk.Button(self.root, text="Получить погоду",font=("Luminari", 16), command=self.get_weather, bg="#FFFCFC", fg="#000000")
        self.search_button.pack(pady=10)
        self.weather_frame = tk.Frame(self.root, bg='#EE7878')
        self.weather_frame.pack(pady=20)
        self.location_label = tk.Label(self.weather_frame, text="", font=("Luminari", 16), bg='#EE7878')
        self.location_label.pack()
        self.temp_label = tk.Label(self.weather_frame, text="", font=("Luminari", 24), bg='#EE7878')
        self.temp_label.pack()
        self.weather_icon = tk.Label(self.weather_frame, bg='#EE7878')
        self.weather_icon.pack()
        self.weather_desc = tk.Label(self.weather_frame, text="", font=("Luminari", 14), bg='#EE7878')
        self.weather_desc.pack()
        self.details_label = tk.Label(self.weather_frame, text="", font=("Luminari", 12), bg='#EE7878')
        self.details_label.pack()
        self.logo_label = tk.Label(self.weather_frame, text="Digital Titan co.", font=("Julius Sans One", 32), bg='#EE7878')
        self.logo_label.pack(pady=20)

    def get_weather(self):
        city = self.city_entry.get()
        if not city:
            messagebox.showwarning("Ошибка", "Пожалуйста, введите название города")
            return
        try:
            complete_url = f"{self.base_url}appid={self.api_key}&q={city}&units=metric&lang=ru"
            response = requests.get(complete_url)
            data = response.json()
            if data["cod"] != 200:
                messagebox.showerror("Ошибка", "Город не найден")
                return
            main_data = data["main"]
            weather_data = data["weather"][0]
            sys_data = data["sys"]
            self.location_label.config(text=f"{data['name']}, {sys_data['country']}")
            self.temp_label.config(text=f"{main_data['temp']}°C")
            self.weather_desc.config(text=weather_data["description"].capitalize())
            icon_url = f"http://openweathermap.org/img/wn/{weather_data['icon']}@2x.png"
            icon_response = requests.get(icon_url)
            icon_data = Image.open(BytesIO(icon_response.content))
            icon = ImageTk.PhotoImage(icon_data)
            self.weather_icon.config(image=icon)
            self.weather_icon.image = icon
            details = (f"Ощущается как: {main_data['feels_like']}°C\n"
                       f"Влажность: {main_data['humidity']}%\n"
                       f"Давление: {main_data['pressure']} hPa\n"
                       f"Ветер: {data['wind']['speed']} м/с")
            self.details_label.config(text=details)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось получить данные о погоде: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg='#FFBDBD')
    app = WeatherApp(root)
    root.mainloop()
