from flask import Flask, flash, g , render_template, request , jsonify
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from datetime import datetime
import os


app = Flask(__name__)

def connect_db():
    sq1=sqlite3.connect('/Users/sambhavjain/Desktop/f1/users.db')
    sq1.row_factory=sqlite3.Row
    return sq1

def get_db():
    if not hasattr(g,'sqlite3_db'):
        g.sqlite_db=connect_db()
        return g.sqlite_db
    
@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'sqlite_db'):
        g.sqlite_db.close()


app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///wholeT.db"
app.config['SQLALCHEMYTRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']='e3ce24acef919e2f8d2a52b9'

    

@app.route ('/')
def hello_world():
    return render_template('index.html',methods=['GET','POST'])
#'''<h1>Hello world</h1>
#<h2>I love to be alone</h2>'''

@app.route('/about/<username>',methods=['GET','POST'])
def about_page(username):
    return f'<h1>This is the about page of {username}</h1>'

@app.route('/help')
def help():
    return "<h2>Help me</h2>"

@app.route('/top_wholesalers.html',methods=['GET','POST'])
def whole():
    return render_template('top_wholesalers.html')

@app.route('/login_page.html', methods=['POST','GET'])
def login():
    if request.method=='POST':
    
        email=request.form.get('email')
        password=request.form.get('password')

        
        db=get_db()
     
        db.execute('insert into login(email,password) values (?,?)', \
            [email,password])
        db.commit()

    return render_template('login_page.html')
     
@app.route('/process1', methods=['POST'])
def process1():
    email=request.form['email']
    password=request.form['password']
    
    return 'Email:{},Password:{}'.format(email,password)

    

@app.route('/json')
def json():
    return jsonify({'key':'value','listkey':[1,2,3]})

@app.route('/signup_page.html',methods=['POST','GET'])
def signup():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        f_name=request.form.get('f_name')
        l_name=request.form.get('l_name')
        address=request.form.get('address')

        db=get_db()

        db.execute('insert into signin(email,password,f_name,l_name,address) values (?,?,?,?,?)', \
            [email,password,f_name,l_name,address])
        
        db.commit()

        
        if len(email)<4:
            flash('Email must be greater than 4 characters.',category='error')
            
        elif len(f_name)<2:
            flash('First Name must be greater than 2 characters.',category='error')
            
        elif len(password)<7:
            flash('Password must be greater than 7 characters.',category='error')
        
        else:
            flash('Account created.')

        
            
    return render_template('signup_page.html')

@app.route('/process', methods=['POST'])
def process():
    email=request.form['email']
    password=request.form['password']
    f_name=request.form['f_name']
    l_name=request.form['l_name']
    cardNo=request.form['cardNo']
    expiry=request.form['expiry']
    address=request.form['address']

    return 'Hello {} {} your address is {} and your email is {} with card number {} and expiry {} with the email {} and password {}'.format(f_name,l_name,address,email,cardNo,expiry,email,password)

@app.route('/verify_now.html',methods=['GET','POST'])
def verify():
    return render_template('verify_now.html')

if __name__=="__main__":
   
    app.run(debug=True)

