class Ticket:
    def __init__(self, ticket_id: str, customer: str, store_name: str, items: list[dict], date: str, details: dict, money_symbology: str="♦") -> None:
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
    
    def get_date(self) -> str:
        """
        Devuelve la fecha del ticket.
        """
        return self.date
    
    def set_date(self, new_date: str) -> None:
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
            "customer" : self.get_customer(),
            "store_name" : self.get_store_name(),
            "items" : self.get_items(),
            "date" : self.get_date(),
            "details" : self.get_details()
        }

        return res
    
    def __repr__(self):
        # Preparamos la lista de items capado a 18 caracteres
        def get_product_data(item: dict, max_chars: int=18):
            name = item["name"]
            count = str(item["count"])
            price = str(item["price"])
            total_chars = len(name) + len(count) + len(price) + len(self.get_money_symbology())
            
            if total_chars + '-' * (max_chars - total_chars) <= max_chars:
                return f"{name}{'-' * (max_chars - total_chars) / 2}{count}{'-' * (max_chars - total_chars) / 2}{price}{self.get_money_symbology()}"
            else:
                return f"{name}\n{count}{'-' * (max_chars - (len(count) + len(price) + len(self.get_money_symbology())))}{price}{self.get_money_symbology()}"
        
        items = ""
        for item in self.get_items():
            items += get_product_data(item, 18) + "\n"
        
        res = f"""==================
{self.get_store_name()}
==================
{self.get_date()}
------------------
Cliente:
  {self.get_customer()}

Productos:
{items}
...

------------------
Detalles:
{self.get_details()['description']}"""
        
        return res

    def get_ticket_obj(self) -> dict:
        """
        Devuelve el ticket en forma de diccionario.
        """
        res = {
            "id" : self.get_ticket_id(),
            "customer" : self.get_customer(),
            "store_name" : self.get_store_name(),
            "items" : self.get_items(),
            "date" : self.get_date(),
            "details" : self.get_details(),
            "money_symbology" : self.get_money_symbology(),
        }

        return res

class Store_Item:
    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        price: int,
        image: str,
        supplier: str,
        labels: list[str] = None,
        stock: int = 0,
        unlimited_stock: bool = False,
    ) -> None:
        self.id = id
        self.name = name
        self.description = description
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

    def get_price(self) -> int:
        """
        Devuelve el precio del item.
        """
        return self.price

    def set_price(self, new_price: int) -> None:
        """
        Establece el nuevo precio del item.
        """
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

    def get_item_obj(self) -> dict:
        """
        Devuelve el item en forma de diccionario.
        """
        res = {
            "id": self.get_id(),
            "name": self.get_name(),
            "description": self.get_description(),
            "price": self.get_price(),
            "image": self.get_image(),
            "supplier" : self.get_supplier(),
            "labels": self.get_labels(),
            "stock": self.get_stock(),
            "unlimited_stock": self.is_unlimited_stock(),
        }

        return res

class Store:
    def __init__(
        self,
        name: str,
        description: str,
        owner: str,
        items: list[Store_Item],
        money: int,
        unlimited_money: bool=True,
        money_symbology: str="♦"
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

    def get_items(self) -> list[Store_Item]:
        """
        Devuelve los items de la tienda.
        """
        return self.items

    def set_items(self, new_items: list[Store_Item]) -> None:
        """
        Establece los nuevos items de la tienda.
        """
        self.items = new_items

    def find_item(self, item: Store_Item) -> bool:
        """
        Comprueba si la tienda tiene un item.
        """
        return item in self.get_items() or item.get_id() in [store_item.get_id() for store_item in self.get_items()]

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

    def set_money(self, new_money) -> None:
        """
        Establece el nuevo dinero que tiene la tienda
        """
        self.money = new_money

    def add_money(self, money) -> None:
        """
        Añade dinero a la tienda.
        """
        self.money += money

    def del_money(self, money) -> bool:
        """
        Elimina dinero de dinero a la tienda. Devuelve False si se pretende quitar más de lo que se tiene.
        """
        if self.get_money() >= money:
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

    def get_money_symbology(self) -> int:
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
        Vende un item y reduce el stock. Si no hay stock, rechaza la venta.
        """
        # Nos aseguramos de que queremos vender una cantidad mayor a 1
        # No tiene sentido vender 0 de algo
        if count < 1:
            print("No se puede vender un item por una cantidad menor a 1.")
            return False

        # Comprobamos que podemos realizar la venta de un item que tenga la tienda
        if self.find_item(item) and item.del_stock(count):
            return self.add_money(item.get_price() * count)

        return False

    def buy_item(self, item: Store_Item, count: int = 1) -> bool:
        """
        Compra un item y aumenta el stock. Si no hay dinero, rechaza la venta.
        """
        # Nos aseguramos de que queremos comprar una cantidad mayor a 1
        # No tiene sentido comprar 0 de algo
        if count < 1:
            print("No se puede vender un item por una cantidad menor a 1.")
            return False

        if self.find_item(item) and (self.is_unlimited_money() or self.get_money() >= item.get_price() * count) and item.add_stock(count):
                return self.del_money(item.get_price() * count)
        
        return False

    def get_store_obj(self) -> dict:
        """
        Devuelve la tienda en forma de diccionario.
        """
        res = {
            "name" : self.get_name(),
            "description" : self.get_description(),
            "owner" : self.get_owner(),
            "items" : [item.get_id() for item in self.get_items()],
            "money" : self.get_money(),
            "unlimited_money" : self.is_unlimited_money()
        }

        return res

# Cada vez que se crea un objeto de alguna de las clases de este módulo, deben guardarse sus datos en la base de datos.