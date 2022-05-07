from flask import render_template
from . import main

# Views
@main.route('/')
def home():

    
    return render_template('index.html' )