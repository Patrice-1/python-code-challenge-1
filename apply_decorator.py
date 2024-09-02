#function named apply_decorator that takes a function func as input and applies a decorator named decorator_func. The decorator should simply print "Decorator Applied" before calling the original function.

def apply_decorator(func):
    def decorator_func(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return decorator_func

# Use apply_decorator to decorate the function
@apply_decorator
def greet(name):
    print(f"Hello, {name}!")

# Test the function
greet("John Wick")

