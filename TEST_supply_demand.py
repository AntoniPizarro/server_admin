from datetime import datetime, timedelta
from pprint import pprint
from random import randint, shuffle

from config import *
from service import MC_Item, MC_Store_DB, MC_Store
from STORE import Ticket
from resources import apply_supply_demand_unlimited_stock

# Constante de stock ilimitado
UNLIMITED_STOCK = True

# Instanciamos la tienda
mc_store = MC_Store(
    name="TEST S.L.",
    description="Tienda para realizar pruebas sobre su funcionalidad y los diferentes items.",
    owner="GPL",
    items=[],
    money=0,
)
mc_store_db = MC_Store_DB(db_cfg["path"])

# Restablecemos la base de datos
mc_store_db.drop_table(ITEM_TABLE)
mc_store_db.drop_table(STORE_TABLE)
mc_store_db.drop_table(TICKET_TABLE)

# Guardamos unos cuantos items en base de datos
items = [
    MC_Item(
        item_id="test_1",
        minecraft_id="minecraft:iron_axe",
        name="Hacha de hierro",
        description="Hacha mejorada para talar madera.",
        base_price=350,
        price=350,
        image="image_test_6",
        supplier=mc_store.get_name(),
        labels=["herramienta", "herramientas", "metal", "hierro", "palo"],
        unlimited_stock=UNLIMITED_STOCK,
    ),
    MC_Item(
        item_id="test_2",
        minecraft_id="minecraft:apple",
        name="Manzana",
        description="Manzana roja procedente de la mismísima Atlantida.",
        base_price=40,
        price=40,
        image="image_test_2",
        supplier=mc_store.get_name(),
        labels=["fruta", "alimentacion", "alimento", "alimentos"],
        unlimited_stock=UNLIMITED_STOCK,
    ),
    MC_Item(
        item_id="test_3",
        minecraft_id="minecraft:diamond_block",
        name="Bloque de diamante",
        description="Bloque compuesto en su totalidad por diamantes.",
        base_price=16000,
        price=16000,
        image="image_test_3",
        supplier=mc_store.get_name(),
        labels=["minerales", "mina", "gema", "gemas", "mineral"],
        unlimited_stock=UNLIMITED_STOCK,
    ),
    MC_Item(
        item_id="test_4",
        minecraft_id="minecraft:ender_pearl",
        name="Perla de ender",
        description="Objeto misterioso que teletransporta al usuario al lugar donde cae.",
        base_price=9600,
        price=9600,
        image="image_test_4",
        supplier=mc_store.get_name(),
        labels=["teletransportacion", "teletransporte", "poder", "magia"],
        unlimited_stock=UNLIMITED_STOCK,
    ),
    MC_Item(
        item_id="test_5",
        minecraft_id="minecraft:wooden_pickaxe",
        name="Pico de madera",
        description="Un pico básico para minar minerales.",
        base_price=50,
        price=50,
        image="image_test_5",
        supplier=mc_store.get_name(),
        labels=["herramienta", "herramientas", "madera", "pico"],
        unlimited_stock=UNLIMITED_STOCK,
    ),
    MC_Item(
        item_id="test_6",
        minecraft_id="minecraft:stone_sword",
        name="Espada de piedra",
        description="Una espada de piedra afilada.",
        base_price=100,
        price=100,
        image="image_test_1",
        supplier=mc_store.get_name(),
        labels=["arma", "armas", "piedra", "espada"],
        unlimited_stock=UNLIMITED_STOCK,
    ),
    MC_Item(
        item_id="test_7",
        minecraft_id="minecraft:golden_apple",
        name="Manzana dorada",
        description="Una manzana dorada, otorga regeneración y resistencia al fuego.",
        base_price=2000,
        price=2000,
        image="image_test_7",
        supplier=mc_store.get_name(),
        labels=["comida", "alimento", "alimentos", "oro", "manzana"],
        unlimited_stock=UNLIMITED_STOCK,
    ),
    MC_Item(
        item_id="test_8",
        minecraft_id="minecraft:diamond_sword",
        name="Espada de diamante",
        description="La espada más poderosa del juego.",
        base_price=15000,
        price=15000,
        image="image_test_8",
        supplier=mc_store.get_name(),
        labels=["arma", "armas", "diamante", "espada"],
        unlimited_stock=UNLIMITED_STOCK,
    ),
    MC_Item(
        item_id="test_9",
        minecraft_id="minecraft:bow",
        name="Arco",
        description="Un arma a distancia que dispara flechas.",
        base_price=250,
        price=250,
        image="image_test_9",
        supplier=mc_store.get_name(),
        labels=["arma", "armas", "distancia", "flecha", "flechas"],
        unlimited_stock=UNLIMITED_STOCK,
    ),
    MC_Item(
        item_id="test_10",
        minecraft_id="minecraft:iron_ingot",
        name="Lingote de hierro",
        description="Un lingote de hierro, material básico para la construcción.",
        base_price=150,
        price=150,
        image="image_test_10",
        supplier=mc_store.get_name(),
        labels=["material", "materiales", "metal", "hierro", "construccion"],
        unlimited_stock=UNLIMITED_STOCK,
    ),
    MC_Item(
        item_id="test_11",
        minecraft_id="minecraft:diamond",
        name="Diamante",
        description="Una gema preciosa y duradera.",
        base_price=5000,
        price=5000,
        image="image_test_11",
        supplier=mc_store.get_name(),
        labels=["gema", "gemas", "mineral", "minerales", "diamante"],
        unlimited_stock=UNLIMITED_STOCK,
    ),
    MC_Item(
        item_id="test_12",
        minecraft_id="minecraft:ender_eye",
        name="Ojo de Ender",
        description="Un objeto que apunta hacia el portal del End.",
        base_price=8000,
        price=8000,
        image="image_test_12",
        supplier=mc_store.get_name(),
        labels=["portal", "ender", "magia", "poder"],
        unlimited_stock=UNLIMITED_STOCK,
    ),
    MC_Item(
        item_id="test_13",
        minecraft_id="minecraft:golden_pickaxe",
        name="Pico de oro",
        description="Un pico de oro, más rápido que el de hierro.",
        base_price=1000,
        price=1000,
        image="image_test_13",
        supplier=mc_store.get_name(),
        labels=["herramienta", "herramientas", "oro", "pico"],
        unlimited_stock=UNLIMITED_STOCK,
    ),
    MC_Item(
        item_id="test_14",
        minecraft_id="minecraft:potion",
        name="Poción",
        description="Una poción con efectos variados.",
        base_price=300,
        price=300,
        image="image_test_14",
        supplier=mc_store.get_name(),
        labels=["pocion", "pociones", "magia", "efecto", "efectos"],
        unlimited_stock=UNLIMITED_STOCK,
    ),
    MC_Item(
        item_id="test_15",
        minecraft_id="minecraft:leather_helmet",
        name="Casco de cuero",
        description="Un casco de cuero para proteger la cabeza.",
        base_price=100,
        price=100,
        image="image_test_15",
        supplier=mc_store.get_name(),
        labels=["armadura", "proteccion", "cuero", "casco"],
        unlimited_stock=UNLIMITED_STOCK,
    ),
    MC_Item(
        item_id="test_16",
        minecraft_id="minecraft:iron_sword",
        name="Espada de hierro",
        description="Una espada de hierro, más fuerte que la de piedra.",
        base_price=300,
        price=300,
        image="image_test_16",
        supplier=mc_store.get_name(),
        labels=["arma", "armas", "metal", "hierro", "espada"],
        unlimited_stock=UNLIMITED_STOCK,
    ),
    MC_Item(
        item_id="test_17",
        minecraft_id="minecraft:diamond_pickaxe",
        name="Pico de diamante",
        description="El pico más eficiente del juego.",
        base_price=12000,
        price=12000,
        image="image_test_17",
        supplier=mc_store.get_name(),
        labels=["herramienta", "herramientas", "diamante", "pico"],
        unlimited_stock=UNLIMITED_STOCK,
    ),
    MC_Item(
        item_id="test_18",
        minecraft_id="minecraft:golden_sword",
        name="Espada de oro",
        description="Una espada de oro, rápida pero frágil.",
        base_price=800,
        price=800,
        image="image_test_18",
        supplier=mc_store.get_name(),
        labels=["arma", "armas", "oro", "espada"],
        unlimited_stock=UNLIMITED_STOCK,
    ),
    MC_Item(
        item_id="test_19",
        minecraft_id="minecraft:stone_axe",
        name="Hacha de piedra",
        description="Un hacha de piedra para talar árboles.",
        base_price=80,
        price=80,
        image="image_test_19",
        supplier=mc_store.get_name(),
        labels=["herramienta", "herramientas", "piedra", "hacha"],
        unlimited_stock=UNLIMITED_STOCK,
    ),
    MC_Item(
        item_id="test_20",
        minecraft_id="minecraft:wooden_sword",
        name="Espada de madera",
        description="Una espada de madera, débil pero fácil de conseguir.",
        base_price=30,
        price=30,
        image="image_test_20",
        supplier=mc_store.get_name(),
        labels=["arma", "armas", "madera", "espada"],
        unlimited_stock=UNLIMITED_STOCK,
    ),
    MC_Item(
        item_id="test_21",
        minecraft_id="minecraft:iron_pickaxe",
        name="Pico de hierro",
        description="Un pico de hierro, más eficiente que el de piedra.",
        base_price=250,
        price=250,
        image="image_test_21",
        supplier=mc_store.get_name(),
        labels=["herramienta", "herramientas", "metal", "hierro", "pico"],
        unlimited_stock=UNLIMITED_STOCK,
    ),
    MC_Item(
        item_id="test_22",
        minecraft_id="minecraft:wooden_axe",
        name="Hacha de madera",
        description="Un hacha básica para talar árboles.",
        base_price=40,
        price=40,
        image="image_test_22",
        supplier=mc_store.get_name(),
        labels=["herramienta", "herramientas", "madera", "hacha"],
        unlimited_stock=UNLIMITED_STOCK,
    ),
    MC_Item(
        item_id="test_23",
        minecraft_id="minecraft:stone_shovel",
        name="Pala de piedra",
        description="Una pala de piedra para cavar tierra.",
        base_price=70,
        price=70,
        image="image_test_23",
        supplier=mc_store.get_name(),
        labels=["herramienta", "herramientas", "piedra", "pala"],
        unlimited_stock=UNLIMITED_STOCK,
    ),
    MC_Item(
        item_id="test_24",
        minecraft_id="minecraft:iron_shovel",
        name="Pala de hierro",
        description="Una pala de hierro, más eficiente que la de piedra.",
        base_price=200,
        price=200,
        image="image_test_24",
        supplier=mc_store.get_name(),
        labels=["herramienta", "herramientas", "metal", "hierro", "pala"],
        unlimited_stock=UNLIMITED_STOCK,
    ),
]
mc_store.add_items(items)
for item in items:
    mc_store_db.add_item(item)

min_date = datetime(2023, 1, 1).toordinal()
max_date = datetime(2025, 12, 31).toordinal()

# Generamos transacciones de compra de los items
# Estas transacciones simulan actividad en la tienda, la cual solo ocurre
# cuando los diferentes clientes compran o venden.
def random_transactions(num_transactions: int):
    for i in range(num_transactions):
        ticket_types = Ticket.get_types()
        if ticket_types:
            ticket_type = ticket_types[randint(0, len(ticket_types) - 1)]
        else:
            ticket_type = "test"
        
        items_copy = items.copy()
        shuffle(items_copy)
        num_items = randint(1, len(items_copy))
        ticket_items = []
        for j in range(num_items):
            item = items_copy.pop()
            ticket_items.append({
                "item_id": item.get_id(),
                "name": item.get_name(),
                "count": randint(1, 128), # La cantidad es aleatoria solo en este test
                "price": item.get_price()
            })
        
        # Ticket con los items aleatorios
        ticket = Ticket(
            ticket_id=datetime.now().isoformat(),
            customer=f"Test_{i}",
            store_name=mc_store.get_name(),
            items=ticket_items,
            date=datetime.fromordinal(randint(min_date, max_date)),
            details={"description" : "Ticket de pruebas", "type" : ticket_type},
            money_symbology="€",
        )

        if mc_store.process_ticket(ticket):
            mc_store_db.add_ticket(ticket)

random_transactions(1000)

print(f"Items: {len(items)}")
for item in mc_store.get_items():
    print(f"{item.get_minecraft_id()} - {item.get_price()} €")

print("=====================")

# Obtenemos los tickets entre dos fechas
day_periode = 30
tickets = mc_store_db.tickets_btween_dates(datetime(2024, 6, 1), datetime(2024, 6, 1) + timedelta(days=day_periode))

print(f"Tickets: {len(tickets)}")
print(f"Desde: {datetime(2024, 6, 1).isoformat()}")
print(f"Hasta: {(datetime(2024, 6, 1) + timedelta(days=day_periode)).isoformat()}")
# Obtenemos los items que han sido tramitados
tramited_items = {}
for ticket in tickets:
    for item_data in ticket.get_items():
        item = mc_store.get_item(item_data["item_id"])
        if item.get_id() not in tramited_items.keys():
            tramited_items[item.get_id()] = {
                "purchases" : item_data["count"] if ticket.get_details()["type"] == "purchases" else 0,
                "sales" : item_data["count"] if ticket.get_details()["type"] == "sales" else 0,
            }
        else:
            tramited_items[item.get_id()][ticket.get_details()["type"]] += item_data["count"]

# Recorremos los items tramitados y aplicamos los nuevos precios en función de la oferta y la demanda
for item_id, data in tramited_items.items():
    item = mc_store.get_item(item_id)
    apply_supply_demand_unlimited_stock(item, data["purchases"], data["sales"])

print("=====================")
print(f"Items tramitados: {len(tramited_items.keys())}")
for item in mc_store.get_items():
    if item.get_id() in tramited_items.keys():
        print(f"{item.get_minecraft_id()} - \t{item.get_base_price()} € / {item.get_price()} € ({item.get_price() - item.get_base_price()} €)")

print("=====================")
for item_id, tramits in tramited_items.items():
    item = mc_store.get_item(item_id)
    print(f"{item.get_minecraft_id()}\t\t{tramits["sales"]} / {tramits["purchases"]}")