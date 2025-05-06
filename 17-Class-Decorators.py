# 17. Class Decorators :

# Assignment:

# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.


def add_greeting(cls):
    # Define a new method to add to the class
    def greet(self):
        return "Hello from Decorator!"
    # Add the greet method to the class
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}."

person = Person("Mohsin Farrukh")
print(person.introduce())  # Existing method in Person
print(person.greet())     
