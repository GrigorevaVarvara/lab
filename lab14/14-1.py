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
    def __init__(self, restaurant_name, rating, flavors):
        super().__init__(restaurant_name, "мороженое", rating)
        self.flavors = flavors

    def display_flavors(self):
        return f"{', '.join(self.flavors)}"
    
stand = IceCreamStand("Мозг замерз", 4.8, ["ваниль", "шоколад", "клубника"])
print(stand.describe_restaurant())
print(stand.display_flavors())