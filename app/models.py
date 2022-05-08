from enum import unique
from sqlalchemy import Column, Integer, PrimaryKeyConstraint
from . import db
class User(db. Model):
    __tablename__='users'
    id= db.Column(db.Integer, primary_key=True) 
    emalil = Column(db.String (255), unique=True, nullable=False)
    username = Column(db.String (255), unique=True, nullable=False)
    
    
    def __repr__(self):
        return f'User {self.username}'
    
    
class Categories():
    ...
    
class Piches:
    ...
    
class Votes():
    ... 
           
class Comments():
    ...    