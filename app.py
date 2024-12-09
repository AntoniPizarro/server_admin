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
    Página inicial.
    '''
    return render_template("index.html")

@app.route("/store", methods=["GET"])
def store():
    '''
    Página de la tienda.
    '''
    return render_template("store.html")

#POST
@app.route("/api/test", methods=["POST"])
def API_test():
    '''
    Método para pruebas
    '''
    data = request.get_json()
    
    return jsonify({"tes" : data})

if __name__ == "__main__":
    app.run(host=API_HOST, debug=True, port=API_PORT)