from flask import render_template
from . import main
from flask_login import login_required
# Views
@main.route('/')
def home():

    
    return render_template('index.html' )