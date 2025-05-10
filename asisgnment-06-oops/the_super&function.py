# Base class
class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person created with name: {self.name}")

# Derived class (Teacher inherits from Person)
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)        # Call parent class constructor
        self.subject = subject
        print(f"Teacher specializes in: {self.subject}")

# Create a Teacher object
t1 = Teacher("Sir Ahmed", "Mathematics")
   # Mathematics
