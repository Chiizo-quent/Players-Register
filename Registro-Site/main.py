from flask import Flask
app = Flask(__name__)

#o bagulho responsável por juntar tudo e fazer o site funcionar.
from views import *
from dataForm import *

# Este código inicia o servidor Flask
if __name__ == "__main__": # Checa se este arquivo é o que foi rodado no terminal, é tipo uma alavanca
    app.run(debug=True) # 'inicia' o  site
