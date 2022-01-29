

# Difference between arguments and parameters
# Parameters are variable that are defined while defining a function inside paranthesis
# Arguments are value that are passed when calling a function
# Difference between positional and keyword arg

print("=== Args and params/ positional and keyword/ Default value ===")


# name -> parameter
# city takes default value
# Default params must be at the end
def print_name(name, age, city="Mumbai"):
    print(name, age, city)
# This gives error
# def print_1(name="23", age):


# Alex -> argument
# Here it is positional arg
# Default can be overwritten
print_name("Alex", 27, "Blr")

# Here it is keyword arg
# In case of keyword arg, order is not important
# default is not necessary to pass
print_name(age=28, name="Jawad")

# Can use mix of both
print_name("Jawad", age=28)

# But using positional args after keyword arg is not allowed, ERROR
# print_name(age=29, "Jawad")

# Assigning same arg as positional and keyword will also raise and error
# print_name("Jawad", name="S")

print("=== Args and Kwargs")
# *args -> One * represent that we can pass any number of positional args
# **kwargs -> Two *'s represent that we can pass any number of key word args
# Instead of args, kwargs it can be any: def(*aa, **bb)


# Here args is tuple
# Her kwargs is dict
def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(kwargs[key])


foo(1, 2, 3, 4, five=5, six=6)
foo(1, 2, 3)
foo(1, 2, three=3)


# Forced keyword only arg
# OR something like: def bar(*, last)
def bar(*args, last):
    for arg in args:
        print(arg)
    print(last)


# This will error as mandatory last args is missing
# bar(1, 2, 3)
bar(1, 2, last=100)

# Unpacking args
print("=== Unpacking arguments ==")


def baz(a, b, c):
    print(a, b, c)


# length of the fn parameter and args should exactly match
my_tuple = (1, 2, 3)
baz(*my_tuple)
my_list = [1, 2, 3]
baz(*my_tuple)
# keys should exactly match, with no more no less
my_dict = {'a': 1, 'b': '2', 'c': 3}
baz(**my_dict)

# Global var
print("=== Global ===")


def foo():
    # This will not affect global `number` variable, this will simply create a local var
    number = 3
    # To modify global var we have to write `global` keyword
    global number_2
    number_2 = 5


number = 1
# If globally number_2 is not defined, the function will make number_2 from fn as global
# So it'll be accessible outside
number_2 = 4
foo()
print(number)
print(number_2)


# Call by value/ref
# In python its call by object or call by obj ref
print("=== Call my reference and value")


# Mutable obj like list and dict be changed within a method, unless we rebind the ref
# immutable obj like int and string cannot be changed within a method
def foo(my_int, my_list_12, my_list_22):
    # Changing my_int will simply create a new local var, it'll not affect global one
    my_int = 2

    # Changing list like this will affect globally passes value as we are
    # modifying the value in reference
    my_list_12.append(4)
    my_list_12[0] = -1
    # Note: This will append the values
    my_list_12 += [5, 6, 7]

    # Note: but this will create a new reference and will not affect outer var
    my_list_22 = my_list_22 + [50, 60, 70]
    # But if we do like this it'll simply create a new local var and global will not be affected
    my_list_22 = [100, 200, 300]


x = 1
y = [1, 2, 3]
z = [12, 22, 32]
foo(x, y, z)
print(x)
print(y)
print(z)

