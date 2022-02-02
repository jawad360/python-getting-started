# https://gitlab.com/nanuchi/python-programming/-/tree/master/
# https://www.youtube.com/watch?v=t8pPdKYpowI&t=19017s&ab_channel=TechWorldwithNana
print(1)
print("Hello world")
# Single and double quote strings are same
print('Hello world 2')
# Int type
print(2)
# Float type
print(3.5)
# Math
print(23*4)
# Concat
# Numbers need to be converted to strings
print("20 days are " + str(20*24*60) + " mins")
# String interpolation
print(f"20 days are {24*60} mins")

# VARIABLES
print("VARIABLES")
# Variables are dynamic typed, so you need have to specify the type
to_seconds = 24 * 60 * 60
print(f"20 days are { 20 * to_seconds } mins")
# Naming convention is generally snake_case

# FUNCTIONS
print("FUNCTIONS")
# PyCharm expect two blank line before and after function call


def days_to_units(num_of_days):
    print(f"{num_of_days} days are { num_of_days * to_seconds } mins")


def days_to_units_with_return(num_of_days):
    return f"{num_of_days} days are { num_of_days * to_seconds } mins"


days_to_units(3)
mess = days_to_units_with_return(1)
print(mess)

# USER INPUT
print("USER INPUT")
# Input is always treated as text
days = input("Enter no of days\n")
days_to_units(days)
# Crashes if user enter days as text/float
days_to_units(int(days))

# CONDITIONS
print("CONDITIONS")


def days_to_units_with_condition(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * to_seconds} mins"
    elif num_of_days == 0:
        return "Enter non zero value"
    else:
        return "enter a positive value"


mess = days_to_units_with_condition(int(input("Enter with condition\n")))
print(mess)

# TRY EXCEPT
print("TRY EXCEPT")


def days_to_unit_with_try(num_of_days):
    try:
        x = int(num_of_days)
        return f"{x} days are {x * to_seconds} mins"
    except ValueError:
        return "Value error"


print(days_to_unit_with_try(input("Enter with try\n")))
