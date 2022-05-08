from flask_sqlalchemy import SQLAlchemy
from . import db
class User(db.Model):
    __tablename__='users'
    id= db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String , unique=True, nullable=False)
    
    
    
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