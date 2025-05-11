
class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    @property
    def price(self):
        """Get the price of the product."""
        return self._price

    @price.setter
    def price(self, value):
        """Set the price of the product."""
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @price.deleter
    def price(self):
        """Delete the price of the product."""
        print("Deleting price...")
        del self._price

# Testing the class
p = Product(500)
print("Initial Price:", p.price)   # Accessing via @property

p.price = 750                      # Updating via @setter
print("Updated Price:", p.price)

del p.price                        # Deleting via @deleter
