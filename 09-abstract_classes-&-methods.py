# 9. Abstract Classes and Methods  :

# Assignment:

# Use the abc module to create an abstract class Shape with an abstractmethod area(). Inherit a class Rectangle that implements area().




#*******************************************************************************************************************
# Abstraction : Hiding complexity and showing only the essentials	Abstract base classes
# Abstraction ka matlab hai unnecessary details ko hide karna aur sirf important information dikhana. Yeh abstract classes aur interfaces ke zariye achieve kiya jata hai.
#*******************************************************************************************************************


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        # Abstract method to calculate area
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        # Implementing the abstract method
        return self.width * self.height
    
rect = Rectangle(5, 10)
print(f"Area of the rectangle: {rect.area()}")    