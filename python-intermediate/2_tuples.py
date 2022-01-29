# Collection data type that is ordered and immutable same is list but just that it cannot be changed after creation
# It allows duplicate
my_tuple = ("Max", 123, "Hello")
print(my_tuple)
print(type(my_tuple))
# parenthesis is optional
my_tuple_1 = "World", "XYZ"
print(my_tuple_1)

# tuple with single element
my_single_1 = ("Hello")
print(type(my_single_1))    # this prints string
my_single_fix = ("Hello",)
print(type(my_single_fix))

# Create using tuple
my_tuple_2 = tuple("Hello")
print(type(my_tuple_2))
my_tuple_3 = tuple(["Hello", "world"])
print(type(my_tuple_3))

# Operations on tuples
print("Operation")
my_index_tuple = (1, 2, 3)
print(my_index_tuple[2])
# my_index_tuple[1] = 4   # This will give error

for i in my_index_tuple:
    print(i)

my_tuple_4 = ('a', 'p', 'p', 'l', 'e')
if 'a' in my_tuple_4:
    print("a present")

# Functions
print("Functions")
# Counts how many times p appeared
print(my_tuple_4.count('p'))
# Returns first index
print(my_tuple_4.index('e'))
# set removes duplicate and is not ordered
print(set(my_tuple_4))

# tuple slicing is same as list slicing
print("Slicing")
slice_1 = my_tuple_4[1:4]
print(slice_1)
# Reverse a list
slice_2 = my_tuple_4[::-1]
print(slice_2)

# Unpacking also know as destructing in js
print("Unpack")
unpack_tuple = (11, 22, 33)
i1, i2, i3 = unpack_tuple
print(i1)
print(i2)
print(i3)
# Unpacking less var will give an error
# i1, i2 = unpack_tuple
# Destructing less variable
unpack_tuple_2 = (11, 22, 33, 44, 55)
i1, *i, il = unpack_tuple_2
print(i)    # this will be a list

my_list = unpack_tuple_2
print(my_list)

# Tuples are efficient to create and takes less memory




