from flask_sqlalchemy import SQLAlchemy
from . import db
class User(db.Model):
    __tablename__='users'
    id= db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String , unique=True, nullable=False)
    
    
    
    def __repr__(self):
        return f'User {self.username}'
    

class Pitch(db.Model):
    __tablename__='pitches'
    id = db.Column(db.Integer, primary_key= True)
    comment = db.relationship('Comment',backref='pitch',lazy='dynamic')
    upvote = db.relationship('Upvote',backref='pitch',lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category = db.Column(db.String(255), index = True,nullable = False) 
    
    def __repr__(self):
        return f'Pitch {self.post}'
    
class Votes(db.Model):
    __tablename__='votes'
    id = db.Column(db.Integer, primary_key= True) 
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    
    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'
           
class Comments(db.Model):
    __tablename__='comments'
    
    id = db.Column(db.Integer, primary_key= True)
    comment = db.Column(db.Text(),nullable = False)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def __repr__(self):
        return f'Comments {self.comment}'
    