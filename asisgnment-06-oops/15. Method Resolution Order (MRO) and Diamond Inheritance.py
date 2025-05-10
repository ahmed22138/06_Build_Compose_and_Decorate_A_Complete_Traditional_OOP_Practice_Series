
class A:
    def show(self):
        print("Show for a class A")

class B(A):
    def show(self):
        print("Show for a class B")
        
class C(A):
    def show(self):
        print("Show for a class C")

class D(B, C):
    pass

obj = D()

obj.show() 

print(D.__mro__) # This will call the show method from class B due to MRO


   