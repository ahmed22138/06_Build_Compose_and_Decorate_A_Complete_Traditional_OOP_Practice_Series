
class Engine:
    def start(slef):
        print("Engine started")

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.engine = Engine()  # Composition: Car has an Engine

    def start(self):
        print(f"{self.make} {self.model} is starting...")
        self.engine.start()  # Delegating the start action to the Engine clas

my_engine = Engine()

my_car = Car("BMW", "M8")

my_car.start()