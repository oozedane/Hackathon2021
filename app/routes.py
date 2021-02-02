import json
from flask import render_template, redirect


from app import app
import random

@app.route('/')
def index():
    return render_template('index.html')














