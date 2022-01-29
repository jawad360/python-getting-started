# One line anonymous function defined without a name
from functools import reduce
# Syntax:
# lambda arguments: expression
add10 = lambda x: x + 10
# Same as
# def add10_func(x): return x + 10
print(add10(3))

mul = lambda x, y: x * y
print(mul(2, 4))

# sorted
point2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
# By default sorts with X coordinate
sorted_list = sorted(point2D)
print(sorted_list)
# Sorting by second tuple value
sorted_list = sorted(point2D, key=lambda x: x[1])
print(sorted_list)
points = [1, 2, 7, 3, -1, 6]
sorted_list_2 = sorted(points)
print(sorted_list_2)

# map(func, seq)
a = [1, 2, 3, 4, 5]
mul2a = map(lambda x: x * 2, a)
print(list(mul2a))
# Using list comprehension
mul2a = [x*2 for x in a]
print(mul2a)

# filter(func, seq)
even = filter(lambda x: x % 2 == 0, a)
print(list(even))
# List comprehension
even = [x for x in a if x % 2 == 0]
print(even)

# reduce(func, seq
prod = reduce(lambda x, y: x * y, a)
print(prod)



