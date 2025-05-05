# 8. The super() Function :

# Assignment:

# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.







#*******************************************************************************************************************
# Inheritance in Python allows us to define a class that inherits all the methods and properties from another class.
#*******************************************************************************************************************

class Person():
    def __init__(self, name):
        self.name = name  # Base class constructor to set the name


class Teacher(Person): 
    def __init__(self, name, subject):
       super().__init__(name)    # Call the base class constructor using super()
       self.subject = subject    

    def display(self):   
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")


teacher = Teacher("Mohsin", "Physics")
teacher.display()  





