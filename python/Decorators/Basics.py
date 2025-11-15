from functools import  wraps
def my_decorators(func):
    @wraps(func)
    def wrapper():
        print("before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorators
def greet():
    print("Hello from the decorators function")
greet()
print(greet.__name__)