from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import InputRequired
  
class PitchForm(FlaskForm):
  title = StringField('Title', validators=[InputRequired()])
  category = SelectField('Category', choices=[('pickup lines','pickup lines'),('Job','Job'),('Advertisement','Advertisement')],validators=[InputRequired()])
  post = TextAreaField('Your Pitch', validators=[InputRequired()])
  submit = SubmitField('Pitch')
  
class CommentForm(FlaskForm):
  comment = TextAreaField('Leave a comment',validators=[InputRequired()])
  submit = SubmitField('Comment')