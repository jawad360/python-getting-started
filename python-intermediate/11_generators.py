# generator returns an object that can be iterated over
# It generates items one at a time and only when asked for it
# It is defined like a normal func but yield instead of return keyword
import sys


def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4


g = my_generator()
# This will executes yield 1 and pause at that point
print(next(g))
# This will continue from yield 1, returns yield 2 and pause there
print(next(g))
print("Loop")
# This will continue
for i in g:
    print(i)

g2 = my_generator()
# This prints the complete list in one go
print(list(g2))
g3 = my_generator()
print(sum(g3))


def count_down(num):
    print("Starting")
    while num >= 0:
        yield num
        num -= 1


cd = count_down(4)
# Only for the first time execution it'll print Starting and then pause after first yield
print(next(cd))
print(next(cd))


# generators are memory efficient as compared to list
def first_n(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


def first_n_gen(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(sys.getsizeof(first_n(100000)))
print(sys.getsizeof(first_n_gen(100000)))

# Generator expression: They are written in same way as list comprehension but with () instead of []
print("Generator expression ")
my_gen = (i for i in range(10) if i % 2 == 0)
for i in my_gen:
    print(i)

