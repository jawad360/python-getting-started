# errors and exception
# Syntax error happens when parser detects syntactically incorrect statement
# TypeError, NameError, ModuleError, FileNotFoundError, ValueError, IndexError, KeyError

# Raising an exception
# x = -5
# if x < 0:
#     raise Exception("x should be positive")
# Asserting
# assert (x >= 0), 'x should be positive'

# try and except. try should always be with except
try:
    a = 5 / 0
except:
    print("An error occured")
# Exceptions as caught in sequence
try:
    a = 5 / 0
    b = 1 + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
# else executes if everything works fine with no exceptions
else:
    print("Everything works fine")
# finally executes always whether exception or not
finally:
    print("Finally executed")

# Custom error
print("== Custom error class ==")


class ValueTooHighError(Exception):
    pass


class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def check_value(x):
    if x > 100:
        raise ValueTooHighError('value too high')
    if x < 5:
        raise ValueTooLowError('value too low', x)


try:
    check_value(40)
except ValueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(e.message, e.value)

