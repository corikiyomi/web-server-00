from flask import Flask, render_template
app = Flask(__name__)
print(__name__)

@app.route('/') # Decorator @
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>') # Dynamic API endpoints to eliminate repetitive code
def html_page(page_name):
    return render_template(page_name)