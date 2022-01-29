# Decorator is a function that takes another function as an argument and extends the behaviour of the function
# there are two decorators function and class decorators
from functools import wraps


def start_end_decorator(func):
    print("Inside Dec")

    def wrapper():
        print('Start')
        func()
        print('End')
    # It needs to be returned because the function using this decorator will be wrapped by wrapper
    return wrapper


def print_name():
    print('Jawad')


# p = start_end_decorator(print_name)
# p()

# With decorator: Dec start_end_decorator is executed and the return of start_end_decorator
# is assigned as print_name_dec function
# Even if we not call print_name_dec() the line 'Inside Doc' is printed


@start_end_decorator
def print_name_dec():
    print('Jawad Dec')


print_name_dec()


# Function With args
print("=== Function with args ===")


def sum_dec(func):
    # to preserve function identify use wrap, wrap is a decorator which take args
    @wraps(func)
    def wrapper(*args, **kwargs):
        result_inner = func(*args, **kwargs)
        return result_inner
    return wrapper


@sum_dec
def sum_1(x):
    return x + 5


result = sum_1(4)
print(result)

# function identity is lost when using decorator
print("Identity", help(sum_1))
print("Name", sum_1.__name__)
# to preserve function identify use wrap

# Decorator with args
print("=== Decorator with args ===")


def repeat(num_times):
    def repeat_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result_inner = func(*args, **kwargs)
            return result_inner
        return wrapper
    return repeat_dec


@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")


greet("Jawad")

# Stacking decorator
print("=== Stacking decorators")


def dec_1(func):
    def wrapper(*args, **kwargs):
        print("Dec 1 start")
        func(*args, **kwargs)
        print("Dec 1 start")
    return wrapper


def dec_2(func):
    def wrapper(*args, **kwargs):
        print("Dec 2 start")
        func(*args, **kwargs)
        print("Dec 2 start")
    return wrapper


# Starts executing dec_1, then dec 2, then func, then compelete dec 2 then dec 1
@dec_1
@dec_2
def say_hello(name):
    print(f"Hello {name}")


say_hello("Jawad")


# Class decorator
print("=== Class decorator ===")


class CountCall:
    def __init__(self, func):
        self.num = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.num += 1
        print(f"Executed {self.num} times")
        self.func(*args, **kwargs)


@CountCall
def say_hello_1():
    print("Hello")


say_hello_1()
say_hello_1()

