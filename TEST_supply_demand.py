from datetime import datetime
from pprint import pprint
from random import randint

from config import *
from service import MC_Item, MC_Store_DB, MC_Store
from STORE import Ticket

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
        base_price=35,
        price=35,
        image="image_test_6",
        supplier=mc_store.get_name(),
        labels=["herramienta", "herramientas", "metal", "hierro", "palo"],
        unlimited_stock=True,
    ),
    MC_Item(
        item_id="test_2",
        minecraft_id="minecraft:apple",
        name="Manzana",
        description="Manzana roja procedente de la mismísima Atlantida.",
        base_price=4,
        price=4,
        image="image_test_2",
        supplier=mc_store.get_name(),
        labels=["fruta", "alimentacion", "alimento", "alimentos"],
        unlimited_stock=True,
    ),
    MC_Item(
        item_id="test_3",
        minecraft_id="minecraft:diamond_block",
        name="Bloque de diamante",
        description="Bloque compuesto en su totalidad por diamantes.",
        base_price=1600,
        price=1600,
        image="image_test_3",
        supplier=mc_store.get_name(),
        labels=["minerales", "mina", "gema", "gemas", "mineral"],
        unlimited_stock=True,
    ),
    MC_Item(
        item_id="test_4",
        minecraft_id="minecraft:ender_pearl",
        name="Perla de ender",
        description="Objeto misterioso que teletransporta al usuario al lugar donde cae.",
        base_price=960,
        price=960,
        image="image_test_4",
        supplier=mc_store.get_name(),
        labels=["teletransportacion", "teletransporte", "poder", "magia"],
        unlimited_stock=True,
    ),
    MC_Item(
        item_id="test_5",
        minecraft_id="minecraft:wooden_pickaxe",
        name="Pico de madera",
        description="Un pico básico para minar minerales.",
        base_price=5,
        price=5,
        image="image_test_5",
        supplier=mc_store.get_name(),
        labels=["herramienta", "herramientas", "madera", "pico"],
        unlimited_stock=True,
    ),
    MC_Item(
        item_id="test_6",
        minecraft_id="minecraft:stone_sword",
        name="Espada de piedra",
        description="Una espada de piedra afilada.",
        base_price=10,
        price=10,
        image="image_test_1",
        supplier=mc_store.get_name(),
        labels=["arma", "armas", "piedra", "espada"],
        unlimited_stock=True,
    ),
    MC_Item(
        item_id="test_7",
        minecraft_id="minecraft:golden_apple",
        name="Manzana dorada",
        description="Una manzana dorada, otorga regeneración y resistencia al fuego.",
        base_price=200,
        price=200,
        image="image_test_7",
        supplier=mc_store.get_name(),
        labels=["comida", "alimento", "alimentos", "oro", "manzana"],
        unlimited_stock=True,
    ),
    MC_Item(
        item_id="test_8",
        minecraft_id="minecraft:diamond_sword",
        name="Espada de diamante",
        description="La espada más poderosa del juego.",
        base_price=1500,
        price=1500,
        image="image_test_8",
        supplier=mc_store.get_name(),
        labels=["arma", "armas", "diamante", "espada"],
        unlimited_stock=True,
    ),
    MC_Item(
        item_id="test_9",
        minecraft_id="minecraft:bow",
        name="Arco",
        description="Un arma a distancia que dispara flechas.",
        base_price=25,
        price=25,
        image="image_test_9",
        supplier=mc_store.get_name(),
        labels=["arma", "armas", "distancia", "flecha", "flechas"],
        unlimited_stock=True,
    ),
    MC_Item(
        item_id="test_10",
        minecraft_id="minecraft:iron_ingot",
        name="Lingote de hierro",
        description="Un lingote de hierro, material básico para la construcción.",
        base_price=15,
        price=15,
        image="image_test_10",
        supplier=mc_store.get_name(),
        labels=["material", "materiales", "metal", "hierro", "construccion"],
        unlimited_stock=True,
    ),
    MC_Item(
        item_id="test_11",
        minecraft_id="minecraft:diamond",
        name="Diamante",
        description="Una gema preciosa y duradera.",
        base_price=500,
        price=500,
        image="image_test_11",
        supplier=mc_store.get_name(),
        labels=["gema", "gemas", "mineral", "minerales", "diamante"],
        unlimited_stock=True,
    ),
    MC_Item(
        item_id="test_12",
        minecraft_id="minecraft:ender_eye",
        name="Ojo de Ender",
        description="Un objeto que apunta hacia el portal del End.",
        base_price=800,
        price=800,
        image="image_test_12",
        supplier=mc_store.get_name(),
        labels=["portal", "ender", "magia", "poder"],
        unlimited_stock=True,
    ),
    MC_Item(
        item_id="test_13",
        minecraft_id="minecraft:golden_pickaxe",
        name="Pico de oro",
        description="Un pico de oro, más rápido que el de hierro.",
        base_price=100,
        price=100,
        image="image_test_13",
        supplier=mc_store.get_name(),
        labels=["herramienta", "herramientas", "oro", "pico"],
        unlimited_stock=True,
    ),
    MC_Item(
        item_id="test_14",
        minecraft_id="minecraft:potion",
        name="Poción",
        description="Una poción con efectos variados.",
        base_price=30,
        price=30,
        image="image_test_14",
        supplier=mc_store.get_name(),
        labels=["pocion", "pociones", "magia", "efecto", "efectos"],
        unlimited_stock=True,
    ),
    MC_Item(
        item_id="test_15",
        minecraft_id="minecraft:leather_helmet",
        name="Casco de cuero",
        description="Un casco de cuero para proteger la cabeza.",
        base_price=10,
        price=10,
        image="image_test_15",
        supplier=mc_store.get_name(),
        labels=["armadura", "proteccion", "cuero", "casco"],
        unlimited_stock=True,
    ),
    MC_Item(
        item_id="test_16",
        minecraft_id="minecraft:iron_sword",
        name="Espada de hierro",
        description="Una espada de hierro, más fuerte que la de piedra.",
        base_price=30,
        price=30,
        image="image_test_16",
        supplier=mc_store.get_name(),
        labels=["arma", "armas", "metal", "hierro", "espada"],
        unlimited_stock=True,
    ),
    MC_Item(
        item_id="test_17",
        minecraft_id="minecraft:diamond_pickaxe",
        name="Pico de diamante",
        description="El pico más eficiente del juego.",
        base_price=1200,
        price=1200,
        image="image_test_17",
        supplier=mc_store.get_name(),
        labels=["herramienta", "herramientas", "diamante", "pico"],
        unlimited_stock=True,
    ),
    MC_Item(
        item_id="test_18",
        minecraft_id="minecraft:golden_sword",
        name="Espada de oro",
        description="Una espada de oro, rápida pero frágil.",
        base_price=80,
        price=80,
        image="image_test_18",
        supplier=mc_store.get_name(),
        labels=["arma", "armas", "oro", "espada"],
        unlimited_stock=True,
    ),
    MC_Item(
        item_id="test_19",
        minecraft_id="minecraft:stone_axe",
        name="Hacha de piedra",
        description="Un hacha de piedra para talar árboles.",
        base_price=8,
        price=8,
        image="image_test_19",
        supplier=mc_store.get_name(),
        labels=["herramienta", "herramientas", "piedra", "hacha"],
        unlimited_stock=True,
    ),
    MC_Item(
        item_id="test_20",
        minecraft_id="minecraft:wooden_sword",
        name="Espada de madera",
        description="Una espada de madera, débil pero fácil de conseguir.",
        base_price=3,
        price=3,
        image="image_test_20",
        supplier=mc_store.get_name(),
        labels=["arma", "armas", "madera", "espada"],
        unlimited_stock=True,
    ),
    MC_Item(
        item_id="test_21",
        minecraft_id="minecraft:iron_pickaxe",
        name="Pico de hierro",
        description="Un pico de hierro, más eficiente que el de piedra.",
        base_price=25,
        price=25,
        image="image_test_21",
        supplier=mc_store.get_name(),
        labels=["herramienta", "herramientas", "metal", "hierro", "pico"],
        unlimited_stock=True,
    ),
    MC_Item(
        item_id="test_22",
        minecraft_id="minecraft:wooden_axe",
        name="Hacha de madera",
        description="Un hacha básica para talar árboles.",
        base_price=4,
        price=4,
        image="image_test_22",
        supplier=mc_store.get_name(),
        labels=["herramienta", "herramientas", "madera", "hacha"],
        unlimited_stock=True,
    ),
    MC_Item(
        item_id="test_23",
        minecraft_id="minecraft:stone_shovel",
        name="Pala de piedra",
        description="Una pala de piedra para cavar tierra.",
        base_price=7,
        price=7,
        image="image_test_23",
        supplier=mc_store.get_name(),
        labels=["herramienta", "herramientas", "piedra", "pala"],
        unlimited_stock=True,
    ),
    MC_Item(
        item_id="test_24",
        minecraft_id="minecraft:iron_shovel",
        name="Pala de hierro",
        description="Una pala de hierro, más eficiente que la de piedra.",
        base_price=20,
        price=20,
        image="image_test_24",
        supplier=mc_store.get_name(),
        labels=["herramienta", "herramientas", "metal", "hierro", "pala"],
        unlimited_stock=True,
    ),
]
mc_store.add_items(items)
for item in items:
    mc_store_db.add_item(item)

min_date = datetime(2023, 1, 1).toordinal()
max_date = datetime(2025, 12, 31).toordinal()


# Generamos transacciones de compra de los items
def random_transactions(num_transactions: int):
    for i in range(num_transactions):
        ticket_items = []
        items_copy = items.copy()
        for j in range(randint(1, len(items_copy))):
            item_index = randint(0, len(items_copy) - 1)

            item = items_copy.pop(item_index)
            ticket_items.append(
                {
                    "item_id": item.get_id(),
                    "name": item.get_name(),
                    "count": randint(1, 128),
                    "price": item.get_price(),
                }
            )

        mc_store_db.add_ticket(
            Ticket(
                datetime.now().isoformat(),
                "TEST",
                mc_store.get_name(),
                ticket_items,
                datetime.fromordinal(randint(min_date, max_date)).isoformat(),
                {"description": "Ticket de pruebas"},
            )
        )


random_transactions(1000)

# Definimos las fechas para buscar los tickets comprendidos entre ellas
date_1 = datetime(2024, 7, 6)
date_2 = datetime(2024, 7, 7)

# Guardamos la lista de tickets
tickets = mc_store_db.tickets_btween_dates(date_1, date_2)

# Mostramos los items que han sido comprados en ese periodo: id, precio actual y cantidad comprada
distinct_items = {}
for ticket in tickets:
    for item in ticket.get_items():
        item_db = mc_store_db.find_items({"id": item["item_id"]})[0]
        if item_db:
            item_obj = mc_store.get_item(item_db["id"])
            
            if not item_obj:
                continue

            if item_obj.get_id() in distinct_items.keys():
                distinct_items[item_db["id"]]["count"] += item["count"]
            else:
                distinct_items[item_db["id"]] = {
                    "count" : item["count"],
                    "minecraft_id" : item_obj.get_minecraft_id(),
                    "price" : item_obj.get_price()
                }

def apply_supply_demand(item: MC_Item, purchases_count: int, sales_count: int, max_price_percentage: float=5000, min_price_percentage: float=2, variance: float=5):
    """
    Cálculo de los precios para generar un sistema de oferta y demanda.

    `indice_demanda = num_compras / (num_ventas + num_compras)`

    `indice_oferta = num_ventas / (num_ventas + num_compras)`

    `precio_final = precio_actual * (1 + indice_demanda - indice_oferta)`

    En caso de no cambiar el precio de un producto durante esos días y habiendo actividad en la tienda, se reducirá el precio en un 5% del precio base de dichos productos. Añadir un factor aleatorio para alterar muy ligeramente el precio durante ese periodo.

    El precio máximo de un producto no puede superar bajo ningún concepto el 5000% del precio original y, por el contrario, un precio no puede ser inferior al 2% del precio original (los porcentajes son valores por defecto con posibilidad de ajuste personalizado).
    """
    if purchases_count == 0 and sales_count == 0 and purchases_count == 0:
        demand_index = 0
        supply_index = 0
    else:
        demand_index = purchases_count / (sales_count + purchases_count)
        supply_index = sales_count / (sales_count + purchases_count)

    final_price = item.get_price() + (item.get_base_price() * (1 + demand_index - supply_index)) - item.get_base_price()
    print(demand_index, supply_index)

    if int(final_price) == item.get_price():
        item.set_price(final_price * (1 - (randint(-variance, variance)) / 100))
    else:
        if final_price >= item.get_base_price() * min_price_percentage / 100:
            item.set_price(final_price)
        else:
            item.set_price(item.get_base_price() * min_price_percentage / 100)

        if final_price <= item.get_base_price() * max_price_percentage / 100:
            item.set_price(final_price)
        else:
            item.set_price(item.get_base_price() * min_price_percentage / 100)

print("=======================")
print(f"ITEMS COMPRADOS entre {date_1} y {date_2}")
for item_id in distinct_items:
    item_db = mc_store_db.find_item({"id": item_id})
    if not item_db:
        print(f"¡¡¡ ID INEXISTENTE !!! -> {item_id}")
        continue

    item = mc_store.get_item(item_id)

    apply_supply_demand(item, distinct_items[item_db["id"]]["count"], 0)

    print(
        {
            "item_id": item_id,
            "minecraft_id": item.get_minecraft_id(),
            "base_price": item.get_base_price(),
            "price": item.get_price(),
            "count": distinct_items[item_db["id"]]["count"],
        }
    )

print("=======================")
print(f"ITEMS NO TRAMITADOS entre {date_1} y {date_2}")
for item in items:
    if item.get_id() not in distinct_items:
        
        apply_supply_demand(item, 0, 0)

        print(
            {
                "item_id": item.get_id(),
                "minecraft_id": item.get_minecraft_id(),
                "base_price": item.get_base_price(),
                "price": item.get_price(),
            }
        )