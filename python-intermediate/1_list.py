# LIST
print("LIST")
mylist = [2, 3, 8, -2, 5, 1]
# Sorting
mylist.sort()
print(mylist)
new_list = sorted(mylist)
print(new_list)
# Generating a list
gen_list = [0] * 5
print(gen_list)
# Concat a list
concat_list = gen_list + new_list
print(concat_list)

# Slice
# [x:y] goes from x till y-1
a = concat_list[3:8]
print(a)
# Jump
b = concat_list[2::2]
print(b)
# Reverse
c = concat_list[::-1]
print(c)

# Copy list
org_list = [1, 2, 3, 4]
# Copies only the reference, not object
cpy_list = org_list
# 1
cpy_list = org_list.copy()
cpy_list.append(5)
print(cpy_list)
# 2
cpy_list = list(org_list)
cpy_list.append(6)
print(cpy_list)
# 3
cpy_list = org_list[:]
cpy_list.append(7)
print(cpy_list)

# Comprehension
sq_list = [i*i for i in org_list]
print(sq_list)


