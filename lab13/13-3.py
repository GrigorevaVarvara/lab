class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating
    
    def describe_restaurant(cls):
        return f"{cls.restaurant_name} - {cls.cuisine_type} - {cls.rating}"
    
    def open_restaurant(cls):
        return f"{cls.restaurant_name} открыт!"
    
    def new_rating(cls, new_rating):
        cls.rating = new_rating
        return f"{cls.restaurant_name} - {cls.cuisine_type} - {cls.rating}"

newRestaurant = Restaurant('Вкусно и не грустно','грузинская',5)
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)
print(newRestaurant.describe_restaurant())
print(newRestaurant.new_rating(4))