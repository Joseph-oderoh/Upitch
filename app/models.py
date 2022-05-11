from flask_login import  UserMixin,current_user
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

    
class User(UserMixin ,db.Model):
    __tablename__='users'
    id= db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String , unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    vote = db.relationship('Vote',backref='user',lazy='dynamic')
    password_hash = db.Column(db.String(255))


    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

class Pitch(db.Model):
    __tablename__='pitches'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255),nullable = False)
    post = db.Column(db.Text(), nullable = False)
    comment = db.relationship('Comment',backref='pitch',lazy='dynamic')
    vote = db.relationship('Vote',backref='pitch',lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    time = db.Column(db.DateTime, default = datetime.utcnow)
    category = db.Column(db.String(255), index = True,nullable = False) 
    
    def save_p(self):
      db.session.add(self)
      db.session.commit()

    def __repr__(self):
        return f'Pitch {self.post}'
    
class Vote(db.Model):
    __tablename__='votes'
    id = db.Column(db.Integer, primary_key= True) 
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_vote(cls,id):
        vote =vote.query.filter_by(pitch_id=id).all()
        return vote
    
    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'
           
class Comment(db.Model):
    __tablename__='comments'
    
    id = db.Column(db.Integer, primary_key= True)
    comment = db.Column(db.Text(),nullable = False)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    
    def save_c(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,pitch_id):
        comments = comments.query.filter_by(pitch_id=pitch_id).all()

        return comments
    def __repr__(self):
        return f'Comments {self.comment}'
