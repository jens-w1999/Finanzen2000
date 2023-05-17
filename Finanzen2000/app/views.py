"""Routing of the Webapp
"""
from app import app
from flask import render_template

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/home")
def home():
    return render_template("home.html")

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