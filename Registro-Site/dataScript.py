from main import app
from flask import request, jsonify
import json 

BASE_DIR = Path(__file__).resolve().parent

@app.route("/checkUser")
def checkUser():
    username = request.args.get('usernameCheck', '')
    caminho = BASE_DIR / "registros" / username
    verify = caminho.is_dir()
    return jsonify({"verify": verify})
