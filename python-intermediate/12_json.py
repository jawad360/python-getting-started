# https://www.python-engineer.com/courses/advancedpython/11-json/
# Python to json format is called serialization

import json

person = {"name": "Jawad", "age": 27, "city": "Mumbai", "hasChildren": False, "titles": ["Engineer", "Developer"]}
print(type(person))

# From dict to json string
person_json = json.dumps(person, indent=4)
print(person_json)
print(type(person_json))

# From dict to file
with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

# From json string to dict
person_1 = json.loads(person_json)
print(person_1)
print(type(person_1))

# From json file to dict
with open("person.json", 'r') as file:
    person_2 = json.load(file)
    print(person_2)
    print(type(person_2))


# Encoding an object
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_user(o):
    return {"name": o.name, "age": o.age}


user = User("Jawad", 27)
user_json = json.dumps(user, default=encode_user)
print(user_json)


# Encoding objects 2
class UserEncoder(json.JSONEncoder):
    def default(self, o):
        return {"name": o.name, "age": o.age}


user_2 = User("Test", 33)
user_json_2 = UserEncoder().encode(user_2)
print(user_json_2)


# decoding json string to object
def decode_user(dict2):
    return User(dict2["name"], dict2["age"])


user_3 = json.loads(user_json_2, object_hook=decode_user)
print(type(user_3))

