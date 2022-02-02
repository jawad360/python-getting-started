# Key-value pair, mutable, unordered
my_dict = {"name": "Jawad", "age": 27, "email": "abc@xyz.com"}
print(my_dict["name"])
# Adding items
my_dict["lastname"] = "Sonalkar"
print(my_dict)
# Modify
my_dict["age"] = 28
print(my_dict)
# Deleting
del my_dict["email"]
print(my_dict)
# Pop
my_dict.pop("age")
print(my_dict)

# Check if item exist
if "name" in my_dict:
    print(f"Name exist: {my_dict['name']}")
try:
    print(my_dict["email"])
except:
    print("Email not found")

# Looping
print("==Looping==")
for key in my_dict:
    print(f"Values: {my_dict[key]}")
for key in my_dict.keys():
    print(f"Keys: {key}")
for val in my_dict.values():
    print(f"Values: {val}")
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# Copying dictionary
print("==COPY==")
org_dist = {"one": 1, "two": 2}
# Only reference is copied, changing copy will change original
copy_dist = org_dist
copy_dist["three"] = 3
print(org_dist)

copy_dist_1 = dict(org_dist)
copy_dist_1["four"] = 4
# It wont be changed here
print(org_dist)

# Tuples can be a dict key, but not list because list is mutable
my_tuple = (1, 2)
my_dict = {my_tuple: 3}
print(my_dict)





