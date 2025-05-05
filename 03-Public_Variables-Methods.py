# 3. Public Variables and Methods :

# Assignment:

# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.


class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):  # Public method
        return f"The {self.brand} car has started."
    
# Instantiate the class
car1 = Car("Toyota")
car2 = Car("Honda")
car3 = Car("Ferrari")
car4 = Car("BMW")
car5 = Car("Mercedes")

# Access public variable
print(f"Car 1 Brand: {car1.brand}")
print(f"Car 2 Brand: {car2.brand}")
print(f"Car 3 Brand: {car3.brand}")
print(f"Car 4 Brand: {car4.brand}") 
print(f"Car 5 Brand: {car5.brand}")

# Access public method
car1.start()
car2.start()    
car3.start()
car4.start()
car5.start()