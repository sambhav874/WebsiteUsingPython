from flask import Flask , render_template
app = Flask(__name__)
import os
@app.route ('/')
def hello_world():
    return render_template('index.html')
#'''<h1>Hello world</h1>
#<h2>I love to be alone</h2>'''

@app.route('/about/<username>')
def about_page(username):
    return f'<h1>This is the about page of {username}</h1>'

@app.route('/help')
def help():
    return "<h2>Help me</h2>"

@app.route('/top_wholesalers.html')
def whole():
    return render_template('top_wholesalers.html')

@app.route('/login_page.html')
def login():
    return render_template('login_page.html')

@app.route('/signup_page.html')
def signup():
    return render_template('signup_page.html')

@app.route('/verify_now.html')
def verify():
    return render_template('verify_now.html')

if __name__=="__main__":
   
    app.run(debug=True)

