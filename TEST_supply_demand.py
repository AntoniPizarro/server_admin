from datetime import datetime
from pprint import pprint

from config import *
from service import MC_Item, MC_Store_DB, MC_Store
from STORE import Ticket

# Instanciamos la tienda
mc_store = MC_Store(
    "TEST S.L.",
    "Tienda para realizar pruebas sobre su funcionalidad y los diferentes items.",
    "GPL",
    [],
    0,
)
mc_store_db = MC_Store_DB(db_cfg["path"])

# Reseteamos la base de datos
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
        price=35,
        image="image_test",
        supplier="TEST S.L.",
        labels=["herramienta", "herramientas", "metal", "hierro", "palo"],
        unlimited_stock=True
    ),
    MC_Item(
        item_id="test_2",
        minecraft_id="minecraft:apple",
        name="Manzana",
        description="Manzana roja procedente de la mismísima Atlantida.",
        price=4,
        image="image_test",
        supplier="TEST S.L.",
        labels=["fruta", "alimentacion", "alimento", "alimentos"],
        unlimited_stock=True
    ),
    MC_Item(
        item_id="test_3",
        minecraft_id="minecraft:diamond_block",
        name="Bloque de diamante",
        description="Bloque compuesto en su totalidad por diamantes.",
        price=1600,
        image="image_test",
        supplier="TEST S.L.",
        labels=["minerales", "mina", "gema", "gemas", "mineral"],
        unlimited_stock=True
    ),
    MC_Item(
        item_id="test_4",
        minecraft_id="minecraft:ender_pearl",
        name="Perla de ender",
        description="Objeto misterioso que teletransporta al usuario al lugar donde cae.",
        price=960,
        image="image_test",
        supplier="TEST S.L.",
        labels=["teletransportacion", "teletransporte", "poder", "magia"],
        unlimited_stock=True
    ),
]
mc_store.add_items(items)
for item in items:
    mc_store_db.add_item(item)

# Generamos transacciones de compra de los items
# Transacción 1
mc_store.send_item(items[0], 2)
mc_store.send_item(items[1], 25)
mc_store.send_item(items[2], 1)
mc_store.send_item(items[3], 6)

ticket_items = [
    {
        "item_id" : items[0].get_id(),
        "name" : items[0].get_name(),
        "count" : 2,
        "price" : items[0].get_price(),
    },
    {
        "item_id" : items[1].get_id(),
        "name" : items[1].get_name(),
        "count" : 25,
        "price" : items[1].get_price(),
    },
    {
        "item_id" : items[2].get_id(),
        "name" : items[2].get_name(),
        "count" : 1,
        "price" : items[2].get_price(),
    },
    {
        "item_id" : items[3].get_id(),
        "name" : items[3].get_name(),
        "count" : 6,
        "price" : items[3].get_price(),
    },
]

mc_store_db.add_ticket(Ticket(datetime.now().isoformat(), "TEST", mc_store.get_name(), ticket_items, datetime(2024, 5, 8).isoformat(), {"description" : "Ticket de pruebas"}))

# Transacción 2
mc_store.send_item(items[0], 1)
mc_store.send_item(items[1], 8)

ticket_items = [
    {
        "item_id" : items[0].get_id(),
        "name" : items[0].get_name(),
        "count" : 2,
        "price" : items[0].get_price(),
    },
    {
        "item_id" : items[1].get_id(),
        "name" : items[1].get_name(),
        "count" : 25,
        "price" : items[1].get_price(),
    },
]

mc_store_db.add_ticket(Ticket(datetime.now().isoformat(), "TEST", mc_store.get_name(), ticket_items, datetime(2024, 7, 1).isoformat(), {"description" : "Ticket de pruebas"}))

# Definimos las fechas para buscar los tickets comprendidos entre ellas
date_1 = datetime(2024, 7, 1)
date_2 = datetime(2024, 7, 31)

# Guardamos la lista de tickets
tickets = mc_store_db.tickets_btween_dates(date_1, date_2)

# Mostramos los items que han sido comprados en ese periodo: id, precio actual y cantidad comprada
print(len(tickets))
if len(tickets) > 0:
    items = []
    for item in tickets[0].get_items():
        item_db = mc_store_db.find_items({"id" : item["item_id"]})
        item_obj = MC_Item(
            item_id=item_db["id"],
            minecraft_id=item_db["minecraft_id"],
            name=item_db["name"],
            description=item_db["description"],
            price=item_db["price"],
            image=item_db["image"],
            supplier=item_db["supplier"],
            labels=item_db["labels"],
            stock=item_db["stock"],
            unlimited_stock=item_db["unlimited_stock"],
        )

        items.append({
            item_obj......
        })

    pprint(items)