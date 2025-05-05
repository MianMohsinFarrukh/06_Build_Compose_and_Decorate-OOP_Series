# 5. Static Variables and Static Methods :

# Assignment:

# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.\

class MathUtils:
    @staticmethod
    def add(a, b):  # Static method
        return a + b
    
result1 = MathUtils.add(50, 50)

print(f"The sum of two numbers is: {result1}")