# Collection: Counter
from collections import Counter, namedtuple, defaultdict, deque
# Counter creates a dict object with key as value and value as count of the keys appearing
# Counter can used with any iterable value like string, list, etc
print("== Counter ==")
my_string = "aaaabbbbbbbvvvcc"
counter = Counter(my_string)
print(counter)
print(list(counter.elements()))
print(counter.most_common(1)[0])

print(type(counter.most_common(1)))
print(type(counter.most_common(1)[0]))

# Returns class
print("== namedtuple ==")
# Creates a Point class with x and y attribute
Point = namedtuple("Point", "x,y")
pt = Point(1, 2)
print(type(pt))
print(pt.x)

print("== defaultdict ==")
# Dict with default value if element accessed is not present
def_dict = defaultdict(int)
def_dict['a'] = 1
# Normal dict will give error in this case, in this case it'll give default value of int
print(def_dict['b'])

print("== deque ==")
dq = deque()
dq.append(1)
dq.append(2)
dq.appendleft(3)
print(dq)
dq.pop()
dq.popleft()
print(dq)
dq.extend([4, 5, 6])
print(dq)
dq.extendleft([1, 2, 3])
print(dq)
dq.rotate(2)
print(dq)

# Unpacking
print("=== Unpacking ===")
number = [1, 2, 3, 4, 5, 6]
# First will always be a list, even if `number` tuple
*first, last = number
print(first)
print(last)

# Merging
# works for list tuple and set
number_2 = [10, 11, 12]
new_num = [*number, *number_2]
print(new_num )
# For dict
dict_1 = {'a': 1, 'b': 2}
dict_2 = {'c': 3, 'd': 4}
new_dict = {**dict_1, **dict_2}
print(new_dict)

