# python-getting-started

## Local Setup Steps

- Create a folder for your project
- Open your folder in your IDE
- Open the terminal in your IDE
- Install virtual environment
    - Mac: `python3 -m pip install --user virtualenv`
    - Windows: `py -m pip install --user virtualenv`
- Create a virtual environment
    - Mac: `python3 -m venv <env>`
    - Windows: `python -m venv <env>`
- Activate your environment
    - Mac: `source ./<env>/bin/activate`
    - Windows: `.\<env>\Scripts\activate`
- Install SQLAlchemy `pip install sqlalchemy`
- Create requirements file `pip freeze > requirements.txt`

- Install dependencies using `pip install -r requirements.txt`
- To come out of virtual env `deactivate`

## Misc
- Install specific version `pip install SQLAlchemy==1.4.31`
- `exit()` to come out of python execution