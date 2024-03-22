from flask import Flask, render_template, request, redirect

app = Flask(__name__)
print(__name__)

@app.route('/') # Decorator @
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>') # Dynamic API endpoints to eliminate repetitive code
def html_page(page_name):
    return render_template(page_name)


#FIXME - Bug 001
'''
Server returns HTTP ERROR 405
'''
@app.route('./templates/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to.dict()
        print(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong. Try again.'