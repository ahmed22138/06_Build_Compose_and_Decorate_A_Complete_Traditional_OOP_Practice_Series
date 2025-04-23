

class car:

    def __init__(self, brand):
     self.brand = brand

    def display(self):
        print(f"{self.brand} Your car is starting...")

my_car = car("BMW")
print("Brand:", my_car.brand)
my_car.display()