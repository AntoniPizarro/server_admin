from datetime import datetime


class Ticket:
    def __init__(
        self,
        ticket_id: str,
        customer: str,
        store_name: str,
        items: list[dict],
        date: datetime,
        details: dict,
        money_symbology: str = "♦",
    ) -> None:
        self.ticket_id = ticket_id
        self.customer = customer
        self.store_name = store_name
        self.items = items
        self.date = date
        self.details = details
        self.money_symbology = money_symbology

    def get_ticket_id(self) -> str:
        """
        Devuelve el ID del ticket.
        """
        return self.ticket_id

    def get_customer(self) -> str:
        """
        Devuelve el cliente del ticket.
        """
        return self.customer

    def set_customer(self, new_customer: str) -> None:
        """
        Establece el cliente del ticket.
        """
        self.customer = new_customer

    def get_store_name(self) -> str:
        """
        Devuelve el nombre de la tienda del ticket.
        """
        return self.store_name

    def set_store_name(self, new_store_name: str) -> None:
        """
        Establece el nombre de la tienda del ticket.
        """
        self.store_name = new_store_name

    def get_items(self) -> list[dict]:
        """
        Devuelve los items del ticket.
        """
        return self.items

    def set_items(self, new_items: list[dict]) -> None:
        """
        Establece los items del ticket.
        """
        self.items = new_items

    def get_date(self) -> datetime:
        """
        Devuelve la fecha del ticket.
        """
        return self.date

    def set_date(self, new_date: datetime) -> None:
        """
        Establece la fecha del ticket.
        """
        self.date = new_date

    def get_details(self) -> dict:
        """
        Devuelve los detalles del ticket.
        """
        return self.details

    def set_details(self, new_details: dict) -> None:
        """
        Establece los nuevos detalles del ticket.
        """
        self.details = new_details

    def get_money_symbology(self) -> dict:
        """
        Devuelve el símbolo monetario del ticket.
        """
        return self.money_symbology

    def set_money_symbology(self, new_money_symbology: dict) -> None:
        """
        Establece el nuevo símbolo monetario del ticket.
        """
        self.money_symbology = new_money_symbology

    def get_ticket_obj(self) -> dict:
        """
        Devuelve el ticket en forma de diccionario.
        """
        res = {
            "customer": self.get_customer(),
            "store_name": self.get_store_name(),
            "items": self.get_items(),
            "date": self.get_date().isoformat(),
            "details": self.get_details(),
        }

        return res

    def __repr__(self):
        # Preparamos la lista de items capado a 20 caracteres
        max_chars = 20

        def get_product_data(item: dict, max_chars: int = max_chars):
            name = item["name"]
            count = f"x{item['count']}"
            price = f"{item['price']}"
            total_chars = (
                len(name)
                + 1
                + len(count)
                + 1
                + len(price)
                + len(self.get_money_symbology())
            )

            if total_chars + len("-" * (max_chars - total_chars)) <= max_chars:
                return f"{name}{'-' * int((max_chars - total_chars) / 2)}{count}{'-' * int(((max_chars - total_chars) / 2) + (max_chars - total_chars) % 2)}{price}{self.get_money_symbology()}"
            else:
                return f"{name}\n{count}{'-' * (max_chars - (2 + len(count) + len(price) + len(self.get_money_symbology())))}{price}{self.get_money_symbology()}"

        items = ""
        for item in self.get_items():
            items += get_product_data(item, max_chars) + "\n"

        res = f"""{'=' * max_chars}
{self.get_store_name()}
{'=' * max_chars}
{self.get_date()}
{'-' * max_chars}
Cliente:
  {self.get_customer()}

Productos:
{items}
...

{'-' * max_chars}
Detalles:
{self.get_details()['description']}"""

        return res

    def get_ticket_obj(self) -> dict:
        """
        Devuelve el ticket en forma de diccionario.
        """
        res = {
            "id": self.get_ticket_id(),
            "customer": self.get_customer(),
            "store_name": self.get_store_name(),
            "items": self.get_items(),
            "date": self.get_date().isoformat(),
            "details": self.get_details(),
            "money_symbology": self.get_money_symbology(),
        }

        return res

    @staticmethod
    def get_types() -> dict:
        """
        Devuelve una lista con los tipos disponibles.
        """
        return ["sales", "purchases"]


class Store_Item:
    def __init__(
        self,
        item_id: str,
        name: str,
        description: str,
        base_price: int,
        price: int,
        image: str,
        supplier: str,
        labels: list[str] = None,
        stock: int = 0,
        unlimited_stock: bool = False,
    ) -> None:
        self.id = item_id
        self.name = name
        self.description = description
        self.base_price = base_price
        self.price = price
        self.image = image
        self.supplier = supplier
        self.labels = labels
        self.stock = stock
        self.unlimited_stock = unlimited_stock

    def get_id(self) -> str:
        """
        Devuelve el ID del item.
        """
        return self.id

    def get_name(self) -> str:
        """
        Devuelve el nombre del item.
        """
        return self.name

    def set_name(self, new_name: str) -> None:
        """
        Establece el nuevo nombre del item.
        """
        self.name = new_name

    def get_description(self) -> str:
        """
        Devuelve la descripción del item.
        """
        return self.description

    def set_description(self, new_description: str) -> None:
        """
        Establece la nueva descripción del item.
        """
        self.description = new_description

    def get_base_price(self) -> int:
        """
        Devuelve el precio base del item.
        """
        return self.base_price

    def set_base_price(self, new_base_price: int) -> None:
        """
        Establece el nuevo precio base del item.
        """
        # Por lo visto, Python acepta otros valores númericos aunque especifiques en tipo
        if type(new_base_price) != int:
            new_base_price = int(new_base_price)

        self.base_price = new_base_price

    def get_price(self) -> int:
        """
        Devuelve el precio del item.
        """
        return self.price

    def set_price(self, new_price: int) -> None:
        """
        Establece el nuevo precio del item.
        """
        # Por lo visto, Python acepta otros valores númericos aunque especifiques en tipo
        if type(new_price) != int:
            new_price = int(new_price)

        self.price = new_price

    def get_image(self) -> str:
        """
        Devuelve la imágen del item.
        """
        return self.image

    def set_image(self, new_image: str) -> None:
        """
        Establece la nueva imágen del item.
        """
        self.image = new_image

    def get_supplier(self) -> str:
        """
        Devuelve el proveedor del item.
        """
        return self.supplier

    def set_supplier(self, new_supplier) -> None:
        """
        Establece el nuevo proveedor del item.
        """
        self.supplier = new_supplier

    def get_labels(self) -> list[str]:
        """
        Devuelve las etiquetas del item.
        """
        return self.labels

    def set_labels(self, new_labels: list[str]) -> None:
        """
        Establece las etiquetas del item.
        """
        self.labels = new_labels

    def add_label(self, new_label: str) -> None:
        """
        Añade una nueva etiqueta al item.
        """
        if new_label not in self.get_labels():
            self.labels.append(new_label)

    def add_labels(self, new_labels: list[str]) -> None:
        """
        Añade nuevas etiquetas al item.
        """
        for new_label in new_labels:
            self.add_label(new_label)

    def del_label(self, label: str) -> None:
        """
        Elimina una etiqueta del item.
        """
        while label in self.get_labels():
            self.labels.remove(label)

    def del_labels(self, labels: list[str]) -> None:
        """
        Elimina etiquetas del item.
        """
        for label in labels:
            self.del_label(label)

    def get_stock(self) -> int:
        """
        Devuelve el stock del item.
        """
        return self.stock

    def set_stock(self, new_stock: int) -> None:
        """
        Establece el nuevo stock del item.
        """
        self.stock = new_stock

    def add_stock(self, new_stock: int = 1) -> bool:
        """
        Añade nuevo stock del item.
        """
        if new_stock > 0 or self.is_unlimited_stock():
            self.stock += new_stock
            return True

        return False

    def del_stock(self, stock: int = 1) -> bool:
        """
        Reduce el stock del item.
        """
        if self.get_stock() >= stock and stock > 0 or self.is_unlimited_stock():
            self.stock -= stock
            return True

        return False

    def is_unlimited_stock(self) -> bool:
        """
        Devuelve si el stock del item es infinito.
        """
        return self.unlimited_stock

    def set_unlimited_stock(self, new_unlimited_stock: bool) -> None:
        """
        Establece si el stock del item es infinito o no.
        """
        self.unlimited_stock = new_unlimited_stock

    def get_item_obj(self, includes: list=None, discarts: list=None) -> dict:
        """
        Devuelve el item en forma de diccionario.
        """
        if discarts == None:
            discarts = []
        
        if includes == None:
            includes = []

        res = {
            "id": self.get_id(),
            "name": self.get_name(),
            "description": self.get_description(),
            "base_price": self.get_base_price(),
            "price": self.get_price(),
            "image": self.get_image(),
            "supplier": self.get_supplier(),
            "labels": self.get_labels(),
            "stock": self.get_stock(),
            "unlimited_stock": self.is_unlimited_stock(),
        }

        # Eliminamos aquellas claves que no se incluyan en la salida
        if len(includes) > 0:
            for key in res.keys():
                if key not in includes:
                    del res[key]

        # Eliminamos aquellas claves que se descartan de la salida
        if len(discarts) > 0:
            for discart in discarts:
                if discart in res.keys():
                    del res[discart]

        return res


class Store:
    def __init__(
        self,
        name: str,
        description: str,
        owner: str,
        items: list[Store_Item],
        money: int,
        unlimited_money: bool = True,
        money_symbology: str = "♦",
    ) -> None:
        self.name = name
        self.description = description
        self.owner = owner
        self.items = items
        self.money = money
        self.unlimited_money = unlimited_money
        self.money_symbology = money_symbology

    def get_name(self) -> str:
        """
        Devuelve el nombre de la tienda.
        """
        return self.name

    def set_name(self, new_name) -> None:
        """
        Establece el nuevo nombre de la tienda.
        """
        self.name = new_name

    def get_description(self) -> str:
        """
        Devuelve la descripción de la tienda.
        """
        return self.description

    def set_description(self, new_description) -> None:
        """
        Establece la nueva descripción de la tienda.
        """
        self.description = new_description

    def get_owner(self) -> str:
        """
        Devuelve el dueño de la tienda. Se recomienda utilizar el nombre de la tienda.
        """
        return self.owner

    def set_owner(self, new_owner) -> None:
        """
        Establece el nuevo dueño de la tienda.
        """
        self.owner = new_owner

    def get_items(self, filters: dict=None) -> list[Store_Item]:
        """
        Devuelve los items de la tienda. Si no hay filtros, se devuelven todos los items.
        """
        if filters == None:
            return self.items
        
        # Creamos una copia de la lista de los items de la tienda y la recorremos
        items = self.items.copy()
        for item in self.items:
            # Inicializamos una variable para comprobar si se descarte cada item
            discarted = True
            
            # Obtenemos los datos de cada item
            item_data = item.get_item_obj(list(filters.keys()))

            # Recorremos los datos del item
            for key, value in item_data.items():
                # Filtro de [ETIQUETAS]
                if key == "labels":
                    # Recorremos las etiquetas indicadas en el filtro
                    for label in filters["labels"]:
                        # Nos aseguramos de que almenos una etiqueta coincide
                        if label in value and item not in items:
                            discarted = False
                # Filtro de [NOMBRE]
                elif key == "name" and "name" in filters.keys():
                    # Nos aseguramos que la palabra filtrada se encuentre en el nombre o la descripción del item
                    if filters["name"] in item.get_name() + item.get_description():
                        discarted = False
                # Filtro de [RANGO DE PRECIOS]
                elif key == "price":
                    # Nos aseguramos que el precio del item se encuentre entre los rangos de precio indicados en el filtro
                    if item.get_price() >= filters[key]["min_price"] and item.get_price() <= filters[key]["max_price"]:
                        discarted = False
                # Cualquier otro filtro
                elif item_data[key] == filters[key] and item not in items:
                    discarted = False
            
            if discarted:
                items.remove(item)

        return items

    def set_items(self, new_items: list[Store_Item]) -> None:
        """
        Establece los nuevos items de la tienda.
        """
        self.items = new_items

    def get_item(self, item_id: str):
        """
        Devuelve un item que tenga la tienda.
        """
        for item in self.get_items():
            if item.get_id() == item_id:
                return item

        return None

    def find_item(self, item: Store_Item) -> bool:
        """
        Comprueba si la tienda tiene un item.
        """
        return item in self.get_items() or item.get_id() in [
            store_item.get_id() for store_item in self.get_items()
        ]

    def add_item(self, new_item: Store_Item) -> None:
        """
        Añade un nuevo item a la tienda.
        """
        if not self.find_item(new_item):
            self.items.append(new_item)
        else:
            print(
                "Se pretende añadir un item que ya tiene la tienda: "
                + new_item.get_name()
            )

    def add_items(self, items: list[Store_Item]) -> None:
        """
        Añade nuevos items a la tienda.
        """
        for item in items:
            self.add_item(item)

    def del_item(self, item: Store_Item) -> None:
        """
        Elimina un item de la tienda.
        """
        if self.find_item(item):
            self.items.remove(item)
        else:
            print(
                "Se pretende eliminar un item que no tiene la tienda: "
                + item.get_name()
            )

    def del_items(self, items: list[Store_Item]) -> None:
        """
        Elimina items de la tienda.
        """
        for item in items:
            self.del_item(item)

    def get_money(self) -> int:
        """
        Devuelve el dinero que tiene la tienda.
        """
        return self.money

    def set_money(self, new_money: int) -> None:
        """
        Establece el nuevo dinero que tiene la tienda
        """
        self.money = new_money

    def add_money(self, money: int) -> None:
        """
        Añade dinero a la tienda.
        """
        if not self.is_unlimited_money():
            self.money += money

    def del_money(self, money: int) -> bool:
        """
        Elimina dinero de dinero a la tienda. Devuelve False si se pretende quitar más de lo que se tiene.
        """
        if self.get_money() >= money or self.is_unlimited_money():
            self.money -= money
            return True

        return False

    def is_unlimited_money(self) -> bool:
        """
        Devuelve si el dinero de la tienda es ilimitado.
        """
        return self.unlimited_money

    def set_unlimited_money(self, new_unlimited_money: bool) -> None:
        """
        Establece si el dinero es ilimitado o no.
        """
        self.unlimited_money = new_unlimited_money

    def get_money_symbology(self) -> str:
        """
        Devuelve el símbolo monetario que tiene la tienda.
        """
        return self.money_symbology

    def set_money_symbology(self, new_money_symbology) -> None:
        """
        Establece el nuevo símbolo monetario que tiene la tienda
        """
        self.money_symbology = new_money_symbology

    def send_item(self, item: Store_Item, count: int = 1) -> bool:
        """
        La tienda vende un item y reduce el stock. Si no hay stock, rechaza la venta.
        """
        # Nos aseguramos de que queremos vender una cantidad mayor a 1
        # No tiene sentido vender 0 de algo
        if count < 1:
            print("No se puede vender un item por una cantidad menor a 1.")
            return False

        # Comprobamos que podemos realizar la venta de un item que tenga la tienda
        if self.find_item(item) and item.del_stock(count):
            money = item.get_price() * count
            self.add_money(money)

            return True

        return False

    def buy_item(self, item: Store_Item, count: int = 1) -> bool:
        """
        La tienda compra un item y aumenta el stock. Si no hay dinero, rechaza la venta.
        """
        # Nos aseguramos de que queremos comprar una cantidad mayor a 1
        # No tiene sentido comprar 0 de algo
        if count < 1:
            print("No se puede vender un item por una cantidad menor a 1.")
            return False

        if (
            self.find_item(item)
            and (
                self.is_unlimited_money()
                or self.get_money() >= item.get_price() * count
            )
            and item.add_stock(count)
        ):
            return self.del_money(item.get_price() * count)

        return False

    def get_store_obj(self) -> dict:
        """
        Devuelve la tienda en forma de diccionario.
        """
        res = {
            "name": self.get_name(),
            "description": self.get_description(),
            "owner": self.get_owner(),
            "items": [item.get_id() for item in self.get_items()],
            "money": self.get_money(),
            "unlimited_money": self.is_unlimited_money(),
        }

        return res

    def process_ticket(self, ticket: Ticket):
        """
        Procesa un ticket según su tipo. En caso de haber un item
        que no se puede vender o comprar, rechaza la operación.
        """
        process_check = True

        # Iteramos sobre los items del ticket
        for item in ticket.get_items():
            item_obj = self.get_item(item["item_id"])

            if ticket.get_details()["type"] == "purchases":
                # Comprobamos que la tienda tiene el item
                if not item_obj and not item_obj.is_unlimited_stock() and not item_obj.get_stock() < item["count"]:
                    print("AAAAA", item_obj)
                    process_check = False
                    break

        # Si todo va bién, procedemos a procesar el ticket
        if process_check:
            for item in ticket.get_items():
                # Comprobamos si el ticket es de venta o compra y realizamos la operación adecuada
                if ticket.get_details()["type"] == "purchases":
                    item_obj = self.get_item(item["item_id"])
                    if not self.send_item(item_obj, item["count"]):
                        print("BBBBB")
                        process_check = False
                elif ticket.get_details()["type"] == "sales":
                    item_obj = self.get_item(item["item_id"])
                    if not self.buy_item(item_obj, item["count"]):
                        print("CCCCC")
                        process_check = False

        if not process_check:
            print(
                f"Ha ocurrido algún problema durante el procesamiento del ticket con ID = {ticket.get_ticket_id()}"
            )

        return process_check


# Cada vez que se crea un objeto de alguna de las clases de este módulo, deben guardarse sus datos en la base de datos.
