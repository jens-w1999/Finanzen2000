"""Routing of the Webapp
"""
from . import app, db
from flask import Flask,render_template, request, redirect, session, url_for, flash
from flask_mysqldb import MySQL
import bcrypt
from datetime import date

# Set secret key for sessions
app.secret_key = b'e2699aed8897f2c4e91eee2cd238adcec98763a1db315653adca2ad056badc9a192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'

def get_hashed_password(plain_text_password):
    # Hash a password for the first time
    #   (Using bcrypt, the salt is saved into the hash itself)
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

def check_password(plain_text_password, hashed_password):
    # Check hashed password. Using bcrypt, the salt is saved into the hash itself
    return bcrypt.checkpw(plain_text_password, hashed_password)

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
    if request.method=='POST':
        cursor = db.connection.cursor()
        email = request.form['email']
        password = request.form['password']
        encrypted_password = password.encode('utf-8')
        query = 'SELECT * FROM Users WHERE email=%s'
        cursor.execute(query, (email,))
        record = cursor.fetchone()

        # check is password is correct
        if check_password(encrypted_password, record[2].encode('utf-8')):
            session['loggedin']= True
            session['email']= record[4]
            session['user_id'] = record[0]
            flash('login successful!')
            cursor.close()
            return redirect(url_for('home'))
        else:
            flash('Invalid login credentials')
        cursor.close()
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('email', None)
    session.pop('user_id', None)
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

        # hash password
        encoded_password = password.encode('utf-8')
        h_password = get_hashed_password(encoded_password)

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
            values = (email, h_password, forename, surname)
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

@app.route("/cost", methods=['GET', 'POST']) 
def cost():
    cursor = db.connection.cursor()

    query = """
    SELECT Transactions.date_from, Transactions.date_to, Transactions.categorie_id, Transactions.amount, Transactions.description, Transactions.update_date, Categories.name 
    FROM Transactions 
    INNER JOIN Users 
    ON Users.id = Transactions.user_id 
    INNER JOIN Transactiontypes 
    ON Transactions.type_id = Transactiontypes.id 
    INNER JOIN Categories 
    ON Transactions.categorie_id = Categories.id 
    WHERE Users.id = %s
    """
    cursor.execute(query, (str(session['user_id']), ))
    data = cursor.fetchall()
    cursor.close()

    if request.method == 'POST' and 'description' in request.form and 'date_to' in request.form:
        user_id = int(session['user_id'])
        date_from = request.form.get('date_from')
        date_to = request.form.get('date_to')
        category = request.form.get('category')
        amount = request.form.get('amount')
        description = request.form.get('description')
        update_date = date.today()
        type_id = 4
        if (date_from != None):
            type_id = 3

        cursor = db.connection.cursor()
        query = 'INSERT INTO Transactions (id, user_id, amount, categorie_id, type_id, date_from, date_to, update_date, description) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s)'
        values = (user_id, amount, category, type_id, date_from, date_to, update_date, description)
        cursor.execute(query, values)
        db.connection.commit()
        cursor.close()
        return render_template('cost.html', output_data = data, dropDown_data = dropdownData)
    return render_template('cost.html', output_data = data, dropDown_data = dropdownData)

@app.route("/addExpense")
def addExpense():
    return render_template("modal_add_Expense.html")

@app.route("/assetManagement")
def assetManagement():
    return render_template('assetManagement.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')