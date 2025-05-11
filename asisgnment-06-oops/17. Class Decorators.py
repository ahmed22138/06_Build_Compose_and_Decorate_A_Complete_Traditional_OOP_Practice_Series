
def add_greeting(cls):
   def greet(self):
       return "Hello from Decoration"
   cls.greet = greet
   return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name 

pi = Person("Ahmed")
print(pi.greet())  # Output: Hello from Decoration
   

