

class Dog:
    def __init__(self, name , breed):
        self.name = name
        self.breed = breed
        
    def bark(self):
        print(f"{self.name} says Woof!")
  

dog1 = Dog("Tommy", "Labrador")
dog2 = Dog("Bruno", "German Shepherd")

# bark() method ko call karte hain
dog1.bark()
dog2.bark()

