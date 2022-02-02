- unicorn is our webserver
- run using `uvicorn main:app --reload`
- Swagger can be accessed using `http://localhost:8000/docs`

Fast api is just a framework to build api, to serve these apis we need a server, FastApi uses uvicorn

Pydantic is python library to perform data validation

redoc is API documentation not interactive can be accessed at `http://localhost:8000/redoc`


Install virtual environment
Mac: python3 -m pip install --user virtualenv
Windows: py -m pip install --user virtualenv


Create a virtual environment
Mac: python3 -m venv env
Windows: python -m venv env


Activate your environment
Mac: source ./env/bin/activate
Windows: .\env\Scripts\activate


Create requirements file pip freeze > requirements.txt