from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "Jawad",
        "age": 27
    }
}


class Student(BaseModel):
    name: str
    age: int


# Simple path
@app.get("/")
def index():
    return "Hello world"


# Path parameter
@app.get("/get-student/{id}")
# description will show info in swagger
# gt, lt are validation, if not meet will throw an exception
def get_student(id: int = Path(None, description="ID of the student", gt=0, lt=3)):
    return students[id]


# Query parameter
@app.get("/get-by-name")
def get_by_name(name: Optional[str] = None):
    for id in students:
        if students[id]["name"] == name:
            return students[id]
    return "Not found"


# Combining both
@app.get("/get-by-id/{student_id}")
def get_by_name(student_id: int, name: Optional[str] = None):
    return students[student_id]


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return "Student existing"
    students[student_id] = student
    return students[student_id]


@app.put("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id not in students:
        return "Student not existing"
    students[student_id] = student
    return students[student_id]


@app.delete("/create-student/{student_id}")
def create_student(student_id: int):
    if student_id not in students:
        return "Student not existing"
    del students[student_id]
    return students
