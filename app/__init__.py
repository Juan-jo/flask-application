from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '3141592653589793238462643383279502884197169399'

#if __name__ == '__main__':
#    app.run(debug=True, host='0.0.0.0', port=3000)

#from app.routers import app