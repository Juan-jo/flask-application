from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '3141592653589793238462643383279502884197169399'
print("Init")

from app.routers import app
