from flask import Flask, render_template
app = Flask(__name__)
print(__name__)

@app.route('/') # Decorator
def my_home():
    return render_template('index.html')

@app.route('/about') # API Endpoint determines what to send to the front end to display the appropriate information
def about_me():
    return render_template('about.html')

@app.route('/contact')
def contact_me():
    return render_template('contact.html')

@app.route('/works')
def my_works():
    return render_template('works.html')
