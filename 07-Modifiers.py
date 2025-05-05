# 7. Access Modifiers: Public, Private, and Protected :

# Assignment:

# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.




#***************************************************************************************************************
# Encapsulation in Python,  Encapsulation is achieved through access modifiers: public, protected, and private.
#***************************************************************************************************************


class Employee():
    def __init__(self, name, salary, ssn):
        self.name = name       # Public variable
        self._salary = salary  # Protected variable
        self.__ssn = ssn       # Private variable   // # Accessing private variable will raise an AttributeError

    def display(self):   # display method  
        print(f"Name: {self.name} \nSalary: {self._salary} \nSSN: {self.__ssn}")

my_variables = Employee('Mohsin', 5000, 123456789) 
print(f"Name : {my_variables.name}")       # Accessing public variable
print(f"Salary : {my_variables._salary}")    # Accessing protected variable
# print(f"ssn : {my_variables.__ssn}")     # Accessing private variable will raise an AttributeError   
        

# Access private variable directly (will raise an error): 
# by using conditions if/else or try/except :
try:
    print(f"Private Variable - SSN: {my_variables.__ssn}")  # Not accessible directly
except AttributeError as e:
    print(f"Error accessing private variable: {e}")

# Access private variable using name mangling
print(f"Private Variable (via name mangling) - SSN: {my_variables._Employee__ssn}") 