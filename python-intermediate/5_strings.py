greeting = """Hello 
World"""
print(greeting)

greeting = """Hello \
World"""
print(greeting)

# Slicing operation same as list

for i in greeting:
    print(i)

if 'World ' in greeting:
    print("World present")

# Methods
my_string = "how,are,you,doing"
my_list = my_string.split(",")
new_string = " ".join(my_list)
print(new_string)

my_list_2 = ['a '] * 6
my_string_2 = ''.join(my_list_2)
print(my_string_2)

# Formatting: %, .format, f-string
name = "Jawad"
# %s - string, %d - int, %f - float
my_string = "Hello %s" % name
print(my_string)

my_string = "Hello {}".format(name)
print(my_string)

my_string = f"Hello {name}"
print(my_string)



