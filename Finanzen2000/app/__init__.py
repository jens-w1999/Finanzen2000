
from flask import Flask
from . import database
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL-Konfiguration
app.config['MYSQL_HOST'] = 'nilstenk.synology.me'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'BudgetMaster'
app.config['MYSQL_PASSWORD'] = 'Ich#Bin#Eine#Robbe13579'
app.config['MYSQL_DB'] = 'budgetmaster'

# MySQL-Verbindung erstellen
mysql = MySQL(app)


from app import views
