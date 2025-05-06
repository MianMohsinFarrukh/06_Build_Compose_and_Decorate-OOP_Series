# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().


def log_function_call(func):
    def wrapper(*args, **kwargs):      #*args (Positional Arguments): **kwargs (Keyword Arguments)
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def say_hello():
    print("Hello, world!")
    
say_hello()
