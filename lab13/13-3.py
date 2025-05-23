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

newRestaurant = Restaurant('Вкусно и не грустно','грузинская',5)
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)
print(newRestaurant.describe_restaurant())
print(newRestaurant.new_rating(4))