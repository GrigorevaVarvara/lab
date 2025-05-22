class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        return f"{self.restaurant_name} - {self.cuisine_type}"
    
    def open_restaurant(self):
        return f"{self.restaurant_name} открыт!"

newRestaurant = Restaurant('Вкусно и не грустно','грузинская')
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)
print(newRestaurant.describe_restaurant())
print(newRestaurant.open_restaurant())