from helloflask import app

from flask import flash, request, render_template, redirect, url_for

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/pic/')
def pic():
    return render_template("picture.html")

@app.route('/form/', methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return render_template("form.html")

    return "Form submited"
