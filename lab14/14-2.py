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
        for ice_type, flavors in self.ice_cream_types.items():
            print(f"{ice_type.capitalize()}: {', '.join(flavors)}")

    def add_flavor_to_type(self, ice_type, flavor):
        flavor = flavor.lower()
        if ice_type in self.ice_cream_types:
            if flavor in self.ice_cream_types[ice_type]:
                print("Такой вкус уже есть в этом типе.")
            else:
                self.ice_cream_types[ice_type].append(flavor)
                print("Вкус добавлен!")
        else:
            print("Такого типа мороженого нет.")

    def delete_flavor_from_type(self, ice_type, flavor):
        flavor = flavor.lower()
        if ice_type in self.ice_cream_types and flavor in self.ice_cream_types[ice_type]:
            self.ice_cream_types[ice_type].remove(flavor)
            print("Вкус удалён.")
        else:
            print("Такого вкуса нет в этом типе.")

    def find_flavor_in_types(self, flavor):
        flavor = flavor.lower()
        for ice_type, flavors in self.ice_cream_types.items():
            if flavor in flavors:
                return f"Вкус '{flavor}' найден в типе '{ice_type}'."
        return "Такого вкуса нет."

    def add_new_type(self, ice_type):
        if ice_type in self.ice_cream_types:
            print("Такой тип уже существует.")
        else:
            self.ice_cream_types[ice_type] = []
            print(f"Тип '{ice_type}' добавлен.")


stand = IceCreamStand("Мозг замерз", 4.8, "Площадь Ленина", "9-21")
print(stand.describe_restaurant())
stand.display_flavors()
stand.add_flavor_to_type("мягкое", "ваниль")
stand.delete_flavor_from_type("на палочке", "шоколад")
print(stand.find_flavor_in_types("банан"))
stand.add_new_type("сливочное")
stand.add_flavor_to_type("сливочное", "карамель")

