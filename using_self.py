

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
      

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

 
student1 = student("Ali", 20)
student2 = student("Ayesha", 92)

student1.display()
student2.display()
