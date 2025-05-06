# 19. callable() and __call__()

# Assignment:

# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.


class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Initialize the factor

    def __call__(self, value):
        """Multiplies the input value by the factor."""
        return value * self.factor

multiplier = Multiplier(10)  # Create an object with factor 5

print("Is 'multiplier' callable?", callable(multiplier))  # Output: True


result = multiplier(10)  
print("Result of multiplier(10):", result)  
