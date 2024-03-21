from flask import Flask, render_template
app = Flask(__name__)
print(__name__)

@app.route('/<username>/<int:post_id>') # Decorator
def hello_world(username=None, post_id=None): # Set the default 
    return render_template('index.html', name=username, post_id=post_id)

@app.route('/blog') # API Endpoint determines what to send to the front end to display the appropriate information
def blog():
    return 'These are my thoughts on blogs'

@app.route('/about')
def about():
    return render_template('about.html')
