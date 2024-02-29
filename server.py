from flask import Flask, render_template
app = Flask(__name__)
print(__name__)

@app.route('/') # Decorator
def hello_world():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return 'These are my thoughts on blogs'

@app.route('/about')
def about():
    return render_template('about.html')