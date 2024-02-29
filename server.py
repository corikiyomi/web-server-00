from flask import Flask, render_template

app = Flask(__name__)
print(__name__)

@app.route('/') # Decorator
def hello_world():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return 'About me'