# 14. Aggregation :

# Assignment:

# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.



class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Position: {self.position}")

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []  # Aggregation: List of Employee objects

    def add_employee(self, employee):
        self.employees.append(employee)  # Adding an Employee reference

    def show_department_details(self):
        print(f"Department: {self.department_name}")
        print("Employees:")
        for employee in self.employees:
            employee.display_details()

emp1 = Employee("Alice", "Software Engineer")
emp2 = Employee("Bob", "Data Analyst")

dept = Department("IT Department")
dept.add_employee(emp1)
dept.add_employee(emp2)

dept.show_department_details()
