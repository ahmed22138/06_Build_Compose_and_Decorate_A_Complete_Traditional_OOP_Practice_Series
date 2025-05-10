
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
            print(f"Employee Name: {self.name}")
            print(f"Employee ID: {self.id}")

class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee # List to hold employees

    def show_details(self):
        print(f"Department: {self.name}") 
        self.employee.display()
        
        
emp1 = Employee("Ahmed", 404)

dept1 = Department("IT" , emp1) 

dept1.show_details()# Displaying employee details