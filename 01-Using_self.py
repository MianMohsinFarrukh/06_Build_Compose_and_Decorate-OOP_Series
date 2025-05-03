# 1. Using self

# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.


class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):   # display method  
        print(f"Name: {self.name} \nMarks:{self.marks}\n")

student_details = Student('Mohsin', 72)
student_details.display()