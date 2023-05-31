"""Routing of the Webapp
"""
from . import app, db
from flask import Flask,render_template, request, redirect, session, url_for, flash
from flask_mysqldb import MySQL

# Set secret key for sessions
app.secret_key = b'e2699aed8897f2c4e91eee2cd238adcec98763a1db315653adca2ad056badc9a192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'

# Beispielroute, um Daten aus der Datenbank abzurufen
@app.route('/testdb')
def testdb():
   cursor = db.connection.cursor()
   cursor.execute("SELECT * FROM Users")  # Ersetzen Sie "table_name" durch den tatsächlichen Tabellennamen
   data = cursor.fetchall()
   cursor.close()
   return str(data)

@app.route("/login", methods=['GET','POST'])
def login():
    cursor = db.connection.cursor()
    query = 'SELECT * FROM Users WHERE email=%s AND password=%s',(email, password)
    if request.method=='POST':
        email = request.form['email']
        password = request.form['password']
        cursor.execute(query)
        record = cursor.fetchone()

        if record:
            session['loggedin']= True
            session['email']= record[4]
            flash('login successful!')
            return redirect(url_for('home'))
        else:
            flash('Invalid login credentials')
    cursor.close()
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('email', None)
    return redirect(url_for('login'))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html", email= session['email'])

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form.get('email')
        password = request.form.get('password')
        password_confirm = request.form.get('password_confirm')
        forename = request.form.get('forename')
        surname = request.form.get('surname')
        cursor = db.connection.cursor()

        # test if user already exists
        test_user_query = 'SELECT COUNT(*) FROM Users WHERE email = %s'
        cursor.execute(test_user_query, (email,))
        result = cursor.fetchone()[0]

        # catch input user errors
        if result > 0:
            flash('Die E-Mail ist bereits registriert.', 'error')
            return render_template('register.html')
        if password == '':
            flash('Bitte gib ein Passwort ein.', 'error')
            return render_template('register.html')
        if email == '':
            flash('Bitte gib eine E-Mail ein.', 'error')
            return render_template('register.html')
        if forename == '':
            flash('Bitte gib einen Namen ein.', 'error')
            return render_template('register.html')
        if surname == '':
            flash('Bitte gib einen Nachnamen ein.', 'error')
            return render_template('register.html')
        if password != password_confirm:
            flash('Die Passwörter stimmen nicht überein.', 'error')
            return render_template('register.html')
        else:
            query = 'INSERT INTO Users (id, email, password, forename, surname) VALUES (NULL, %s, %s, %s, %s)'
            values = (email, password, forename, surname)
            cursor.execute(query, values)
            db.connection.commit()
            cursor.close()
            db.connection.close()
            return redirect(url_for('login'))
        
    return render_template('register.html')

@app.route("/overview")
def overview():
    return render_template('overview.html')

@app.route("/income")
def income():
    return render_template('income.html')

@app.route("/cost") 
def cost():
    return render_template('cost.html')

@app.route("/assetManagement")
def assetManagement():
    return render_template('assetManagement.html')