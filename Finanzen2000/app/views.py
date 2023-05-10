"""Routing of the Webapp
"""
from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/register")
def register():
    return "Hello world"