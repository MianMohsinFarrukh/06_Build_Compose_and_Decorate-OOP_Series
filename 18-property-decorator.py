# 18. Property Decorators: @property, @setter, and @deleter

# Assignment:

# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.


class Product:
    def __init__(self, price):
        self._price = price  

    @property
    def price(self):
        """Getter: Retrieve the price."""
        return self._price

    @price.setter
    def price(self, value):
        """Setter: Update the price."""
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self._price = value

    @price.deleter
    def price(self):
        """Deleter: Delete the price."""
        print("Deleting price...")
        self._price = None

product = Product(200)

# Accessing the price
print("Initial Price:", product.price)

# Updating the price
product.price = 150
print("Updated Price:", product.price)

# Deleting the price
del product.price
print("Price after deletion:", product.price)
