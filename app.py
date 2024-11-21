from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

from service import *

app = Flask(__name__, template_folder='./web_site/templates/', static_folder="./web_site/static/")
CORS(app)

API_HOST = "0.0.0.0"
API_PORT = 5500

# GET
@app.route("/", methods=["GET"])
def home():
    '''
    'Página inicial.
    '''
    return render_template("index.html")

@app.route("/test", methods=["GET"])
def testttt():
    '''
    'Página inicial.
    '''
    return render_template("test.html")

@app.route("/installer", methods=["GET"])
def installer():
    '''
    'Página del tutorial sobre el instalador.
    '''
    return render_template("installer.html")

@app.route("/store", methods=["GET"])
def store():
    '''
    'Página de la tienda.
    '''
    return render_template("store.html")

#POST
@app.route("/api/skins/set/<password>", methods=["POST"])
def API_set_skin(password):
    '''
    'Asignar skin a un jugador
    '''
    cant_set_skin = [""]
    
    data = request.get_json()
    res = False
    if password == "avellana9-":
        res = set_player_skin(data["player"], data["skin_url"]) not in cant_set_skin
    
    return jsonify({"skin" : res})

if __name__ == "__main__":
    app.run(host=API_HOST, debug=True, port=API_PORT)