import requests

res = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
projects = res.json()
print(type(projects))

for project in projects:
    print(f"Id: {project['id']} Name: {project['name']}")


