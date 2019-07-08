from app import app
from flask import render_template

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def hello_world():
    return render_template('layaut.html')
