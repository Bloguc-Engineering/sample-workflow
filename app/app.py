""" Sample python code"""
from flask import Flask

app = Flask(__name__)
""" Defineing route """
@app.route('/')
def hello_world():
    """Funtion for getting response"""
    return 'Hello, World!'
if __name__ == '__main__':
    app.run()
