from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

from service import *
from config import *

API_HOST = "0.0.0.0"
API_PORT = 5500

app = Flask(__name__, template_folder='./web_site/templates/', static_folder="./web_site/static/")
CORS(app)

# Constante de stock ilimitado
UNLIMITED_STOCK = True

# Instanciamos los controladores de base de datos
mc_store_db = MC_Store_DB(db_cfg["path"])
data_db = Data_DB(db_cfg["path"])

# Instanciamos la tienda
store_data = data_db.get_data(DATA_ID)

items_data = mc_store_db.get(ITEM_TABLE)
items = []
for item_data in items_data:
    item = MC_Item.from_item_data(item_data)
    if item != None:
        items.append(item)

mc_store = MC_Store(
    name=STORE_NAME,
    description=STORE_DESCRIPTION,
    owner=STORE_OWNER,
    items=items,
    money=store_data["money"],
)

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
@app.route("/api/items", methods=["POST"])
def API_items():
    '''
    Devuelve los items de la tienda aplicando filtros.
    '''
    data = request.get_json()

    filters = data["item_filters"]
    if type(filters) != dict or len(filters.keys()) == 0:
        filters = None
    
    items = mc_store.get_items(filters)
    res = []
    for item in items:
        res.append(item.get_item_obj(discarts=["id"]))
    
    return jsonify(res)

@app.route("/api/test", methods=["POST"])
def API_test():
    '''
    Método para pruebas
    '''
    data = request.get_json()
    
    return jsonify({"tes" : data})

if __name__ == "__main__":
    app.run(host=API_HOST, debug=True, port=API_PORT)