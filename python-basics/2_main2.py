# LOOPS
print("LOOPS ")


def echo_days(num_of_days):
    print(f"{num_of_days} days")


user_input = ""
while user_input != "exit":
    user_input = input("Enter days or exit\n")
    echo_days(user_input)


user_input_list = input("Enter list\n")
for el in user_input_list.split(","):
    echo_days(el)

# LIST
print("LIST")
num_list = [1, 2, 3]
print(num_list)
num_list.append(4)
print(len(num_list))
num_list.remove(4)
print(num_list[1])
# print(f"Error {num_list[4]}") out of range
# prints last element
print(num_list[-1])

# SET: List with no duplicates
# Items in set do have have an order. It cannot be referred by index
# Items in set cannot be changed, it can be added or removed
mon_set = {"Jan", "Feb", "Feb"}
print(mon_set)      # it'll print {'Jan', 'Feb'}
mon_set_1 = set(num_list)
# Elements can be accessed by loops
for mon in mon_set:
    # printing order will be changed, it'll be random
    print(mon)
mon_set.add("Mar")
# Print order will be random
print(mon_set)
mon_set.remove("Mar")

# DICTIONARY: It's an object
print("DICTIONARY")
days_and_units = {"days": 12, "unit": "hours"}
print(days_and_units.get("days"))
print(days_and_units["unit"])
days_and_units["message"] = "Hello"
print(days_and_units)
