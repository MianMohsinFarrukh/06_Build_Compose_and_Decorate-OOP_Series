# 13. Composition :

# Assignment:

# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.


class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} horsepower is starting...")

    def stop(self):
        print("Engine is stoped!")


class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # Composition: Car has an Engine

    def start_car(self):
        print(f"{self.brand} car is starting...")
        self.engine.start()  # Accessing Engine's method via Car

    def stop_car(self):
        print(f"{self.brand} car is stopping...")
        self.engine.stop()  # Accessing Engine's method via Car


# Example usage
engine = Engine(1800)
car = Car("Toyota", engine)

car.start_car()
car.stop_car()

