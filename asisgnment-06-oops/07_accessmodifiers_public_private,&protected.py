

class employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

    def display(self):
        print("Name:", self.name)
        print("Salary:", self._salary)
        print("SSN:", self.__ssn)

emp = employee("Ali", 50000, "123-45-6789")

print("Public Access:", emp.name)       
print("Protected Access:", emp._salary) 

try:
    print("Private Access:", emp.__ssn)
except AttributeError as e:
    print("Private Access Error:", e)

# Optional trick (not good practice)
print("Access via name mangling:", emp._employee__ssn)
