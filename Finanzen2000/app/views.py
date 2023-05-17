"""Routing of the Webapp
"""
from . import app, db
from flask import Flask,render_template, request, redirect, session, url_for

# Set secret key for sessions
app.secret_key = b'e2699aed8897f2c4e91eee2cd238adcec98763a1db315653adca2ad056badc9a192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'

# Beispielroute, um Daten aus der Datenbank abzurufen
@app.route('/testdb')
def index():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM Users")  # Ersetzen Sie "table_name" durch den tatsächlichen Tabellennamen
    data = cursor.fetchall()
    cursor.close()
    return str(data)

@app.route("/login", methods=['GET','POST'])
def login():
    cursor = db.connection.cursor()
    msg=''
    if request.method=='POST':
        email = request.form['email']
        password = request.form['password']
        cursor.execute('SELECT * FROM Users WHERE email=%s AND password=%s',(email, password))
        record = cursor.fetchone()

        if record:
            session['authentificated']= True
            session['email']= record[4]
            return redirect(url_for('home'))
        else:
            msg='Falsche E-Mail oder Passwort. Versuchs nochmal.'
    return render_template('login.html')

@app.route("/home")
def home():
    return render_template("home.html", email= session['email'])

@app.route("/register")
def register():
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