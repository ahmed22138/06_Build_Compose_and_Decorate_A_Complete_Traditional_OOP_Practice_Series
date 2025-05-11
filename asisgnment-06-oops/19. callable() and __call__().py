
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value
    
# Example usage
triple = Multiplier(10)

print(callable(triple))

result = triple(9)  # Calls the __call__ method
print(result)
        