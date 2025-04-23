

class mathUtils:
    # Static variable
    @staticmethod
    def add(a, b):  # Static method
        return a + b
    
    # Call the static method
print(mathUtils.add(10, 5))   # Output: 15

# 2. Object banakar bhi (lekin zaroori nahi)
utils = mathUtils()
   
print(utils.add(7, 3)) # OUtput: 10
# 3. Class se bhi call kar sakte hain (lekin zaroori nahi)
