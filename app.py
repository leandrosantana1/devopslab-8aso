from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Esta pipeline taaaaa um sucesso"

if __name__ == '__main__':
    app.run()