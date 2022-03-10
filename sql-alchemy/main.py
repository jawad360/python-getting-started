from sqlalchemy import Column, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = 'user'
    username = Column('user_name', String, primary_key=True)
    password = Column('password', String, primary_key=True)

engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

session = Session()

user = User(username="jawad", password="some_password")
user2 = User(username="test", password="nother_password")
session.add(user)
session.add(user2)
session.commit()

users = session.query(User).all()
for u in users:
    print(u.username)

session.close()