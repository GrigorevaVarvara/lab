import tkinter as tk
from tkinter import messagebox, simpledialog

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        return f"{self.restaurant_name} - {self.cuisine_type} - {self.rating}"

    def open_restaurant(self):
        return f"{self.restaurant_name} открыт!"

    def new_rating(self, new_rating):
        self.rating = new_rating
        return f"{self.restaurant_name} - {self.cuisine_type} - {self.rating}"

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, rating, location, time_open):
        super().__init__(restaurant_name, "мороженое", rating)
        self.location = location
        self.time_open = time_open
        self.ice_cream_types = {
            "на палочке": ["ваниль", "шоколад"],
            "мягкое": ["клубника", "банан"],
            "фруктовый лёд": ["малина", "лимон"]
        }

    def display_flavors(self):
        return "\n".join(
            f"{ice_type.capitalize()}: {', '.join(flavors)}"
            for ice_type, flavors in self.ice_cream_types.items()
        )

    def add_flavor_to_type(self, ice_type, flavor):
        flavor = flavor.lower()
        if ice_type in self.ice_cream_types:
            if flavor in self.ice_cream_types[ice_type]:
                return "Такой вкус уже есть"
            else:
                self.ice_cream_types[ice_type].append(flavor)
                return "Вкус добавлен!"
        else:
            return "Такого типа мороженого нет"

    def delete_flavor_from_type(self, ice_type, flavor):
        flavor = flavor.lower()
        if ice_type in self.ice_cream_types and flavor in self.ice_cream_types[ice_type]:
            self.ice_cream_types[ice_type].remove(flavor)
            return "Вкус удалён"
        else:
            return "Такого вкуса и не было"

    def find_flavor_in_types(self, flavor):
        flavor = flavor.lower()
        for ice_type, flavors in self.ice_cream_types.items():
            if flavor in flavors:
                return f"Вкус '{flavor}' найден в типе '{ice_type}'."
        return "Такого вкуса нет"

    def add_new_type(self, ice_type):
        if ice_type in self.ice_cream_types:
            return "Такой тип уже существует"
        else:
            self.ice_cream_types[ice_type] = []
            return f"Тип '{ice_type}' добавлен"

stand = IceCreamStand("Мозг замерз", 4.8, "Площадь Ленина", "9-21")
root = tk.Tk()
root.title("Ларёк мороженого — Мозг замерз")
root.geometry("500x500")
root.configure(bg="#e0f7fa") 

roof_canvas = tk.Canvas(root, width=500, height=120, bg="#e0f7fa", highlightthickness=0)
roof_canvas.pack()
roof_canvas.create_polygon(
    0, 120, 250, 20, 500, 120,
    fill="#f06292", outline="#ad1457", width=3
)
roof_canvas.create_rectangle(150, 65, 350, 100, fill="#fff3e0", outline="#6d4c41", width=2)
roof_canvas.create_text(250, 83, text="Мозг замерз", font=( 14), fill="#d81b60")

frame_display = tk.LabelFrame(root, width=500, text="Витрина", bg="#fce4ec", fg="#880e4f", font=(12))
frame_display.pack(fill="y")

text_display = tk.Text(frame_display, width=50, height=10, bg="#fff", fg="#4a148c", font=(12))
text_display.pack(padx=10, pady=10)

frame_buttons = tk.Frame(root, bg="#e0f7fa")
frame_buttons.pack(pady=10)

def update_display():
    text_display.delete("1.0", tk.END)
    text_display.insert(tk.END, stand.display_flavors())

def add_flavor():
    ice_type = simpledialog.askstring("Добавить вкус", "Введите тип мороженого:")
    flavor = simpledialog.askstring("Добавить вкус", "Введите вкус:")
    if ice_type and flavor:
        msg = stand.add_flavor_to_type(ice_type.lower(), flavor.lower())
        messagebox.showinfo("Результат", msg)
        update_display()

def delete_flavor():
    ice_type = simpledialog.askstring("Удалить вкус", "Введите тип мороженого:")
    flavor = simpledialog.askstring("Удалить вкус", "Введите вкус:")
    if ice_type and flavor:
        msg = stand.delete_flavor_from_type(ice_type.lower(), flavor.lower())
        messagebox.showinfo("Результат", msg)
        update_display()

def add_type():
    ice_type = simpledialog.askstring("Новый тип", "Введите новый тип мороженого:")
    if ice_type:
        msg = stand.add_new_type(ice_type.lower())
        messagebox.showinfo("Результат", msg)
        update_display()

def find_flavor():
    flavor = simpledialog.askstring("Поиск вкуса", "Введите вкус:")
    if flavor:
        msg = stand.find_flavor_in_types(flavor.lower())
        messagebox.showinfo("Результат", msg)

tk.Button(frame_buttons, text="Добавить вкус", command=add_flavor, bg="#f8bbd0").grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_buttons, text="Удалить вкус", command=delete_flavor, bg="#ffccbc").grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_buttons, text="Новый тип", command=add_type, bg="#c8e6c9").grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame_buttons, text="Найти вкус", command=find_flavor, bg="#d1c4e9").grid(row=1, column=1, padx=5, pady=5)

update_display()
root.mainloop()
