from main import app
from flask import render_template
# Este arquivo é responsável pra levar para as páginas do site
@app.route("/") # vai levar para página inicial do site
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")