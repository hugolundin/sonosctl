from . import main
from flask import render_template, url_for, redirect

@main.route('/', methods=['GET'])
def index():
    return render_template('main/index.html')
