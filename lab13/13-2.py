class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(cls):
        return f"{cls.restaurant_name} - {cls.cuisine_type}"
    
    def open_restaurant(cls):
        return f"{cls.restaurant_name} открыт!"

newRestaurant = Restaurant('Вкусно и не грустно','грузинская')
newRestaurant2 = Restaurant('У жмурика','убийственная')
newRestaurant3 = Restaurant('Только гречка','гречка')
print(newRestaurant.describe_restaurant())
print(newRestaurant2.describe_restaurant())
print(newRestaurant3.describe_restaurant())
