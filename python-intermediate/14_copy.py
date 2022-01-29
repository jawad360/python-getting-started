from copy import copy, deepcopy

org = 5
# This will not create a new var, it'll just point the ref to `org`
cpy = org
# Now this will create a new var
cpy = 6

# Shallow copy: It copies only one level deep
my_list = [1, 2, 3]
# copy method works for object also
cpy_list = copy(my_list)
# cp = my_list.copy()
# cp = list(my_list)
# cp = my_list[:]
cpy_list[0] = -100
print(cpy_list)
print(my_list)

# Deep copy
my_list_1 = [[1, 2], [3, 4]]
cpy_list_1 = deepcopy(my_list_1)
my_list_1[0][1] = -100
print(cpy_list_1)
print(my_list_1)

