# 10. Instance Methods :

# Assignment:

# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

#***************************************************************************************
# Polymorphism	Methods behaving differently for subclasses	Dog and Cat overriding speak.
#***************************************************************************************

class Dog():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} the {self.breed} says Woof!")  #insatance method


       
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Charlie", "Poodle")

# Call the instance method
dog1.bark()
dog2.bark()