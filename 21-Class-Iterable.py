# 21. Make a Custom Class Iterable

# Assignment:

# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.


class Countdown:
    def __init__(self, start):
        self.current = start  # Initialize the starting number

    def __iter__(self):
        """Return the iterator object (self)."""
        return self

    def __next__(self):
        """Return the next value in the iteration."""
        if self.current < 0:  # Stop iteration when the value is below 0
            raise StopIteration
        value = self.current
        self.current -= 1  # Decrement the current number
        return value


countdown = Countdown(5)

print("Countdown using for-loop:")
for number in countdown:
    print(number)


print("\nCountdown using manual iteration:")
countdown_manual = Countdown(3)
iterator = iter(countdown_manual)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
