from flask import Flask

app = Flask(__name__)
print(__name__)

@app.route('/') # Decorator
def hello_world():
    return '<p>Hello, World!</p>'