'''House all the application routes

Author: Ukor, Jidechi
Organization: Tedx Ebonyi State
Maintainers: []
'''

from flask import render_template, url_for
from tedxEbonyiState import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/speakers')
def speakers():
    return render_template('speakers_2019.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')
