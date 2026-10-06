from main import app
from flask import request, render_template
from pathlib import Path
#BAAAANACO de dados do site
BASE_DIR = Path(__file__).resolve().parent  

@app.route("/FazerLogin", methods=["POST"])
def FazerLogin():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    print(username)
    print(password)
    return render_template("login.html")

@app.route("/FazerCadastro", methods=["POST"])
def FazerCadastro():
    username = request.form.get('username', '')
    password = request.form.get('password', '')

    caminho = BASE_DIR / "registros" / username
    if caminho.is_dir():
        return render_template("cadastro.html")
    caminho.mkdir(parents=True)
    with open(BASE_DIR / "registros" / username / "Senha.txt", 'w') as f: # w -> write; a -> append
        f.write(password)
    return render_template("cadastro.html")