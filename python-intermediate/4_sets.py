# Sets are unordered, mutable and non duplicate
my_set = {1, 2, 3}
# Sets can be created using list or string
my_set_1 = set([1, 2, 3])
my_set_2 = set("Hello")
# This prints {'l', 'o', 'H', 'e'}
print(my_set_2)

# Add remove
print("== Add remove ==")
# this will not create and empty set, but will create and dict
my_set = {}
# Creating empty set
my_set = set()
my_set.add(1)
my_set.add(2)
print(my_set)
# This will give error
# my_set.remove(3)
# This will not give error
my_set.discard(3)
my_set.discard(2)
print(my_set)

# Removes random element
print(my_set.pop())

# Loop and if
print("== Loop and if ==")
my_set = {1, 2, 3, 4}
if 1 in my_set:
    print("1 is present")
for x in my_set:
    print(x)

# Operation
print("== Operation ==")
even = {2, 4, 6, 8}
odd = {1, 3, 5, 7}
prime = {1, 2, 3, 5, 7, 11}
# These operations do no mutate the source set
print(f"Union: {even.union(odd)}")
print(f"Intersection: {even.intersection(odd)}")
print(f"Intersection: {odd.intersection(prime)}")
print(f"Difference: {prime.difference(odd)}")
print(even)
print(odd)

# To mutate the source set we can use update
prime.update(even)
print(prime)
even.intersection_update(odd)
print(even)
prime.difference_update(odd)
print(prime)

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
print(setA.issuperset(setB))
print(setB.issubset(setA))

# Copy
print("== Copy ==")
# This will just copy the reference
setA = setB
# This will change set B as well
setA.add(7)
print(setB)

# To copy
setC = setA.copy()
setC.add(11)
print(setA)
print(setC)
# or
setD = set(setA)

# to create immutable set use
immut_set = frozenset(setA)
print(immut_set)
immut_set.add(12)
