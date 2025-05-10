from abc import ABC, abstractmethod

# Step 1: Abstract class banai
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Bas function define kiya, koi code nahi diya

# Step 2: Rectangle class jo Shape se inherit karti hai
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Step 3: Object banate hain aur area nikalte hain
rect = Rectangle(5, 3)
print("Area of rectangle:", rect.area())
