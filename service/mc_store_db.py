from datetime import datetime

from .db import Data_Base as DB
from .minecraft_store import MC_Item, Ticket, Store
from config import STORE_TABLE, ITEM_TABLE, TICKET_TABLE, CATHEGORIES_TABLE

class MC_Store_DB(DB):
    def __init__(self, host):
        super().__init__(host)
    
    def add_store(self, store: Store) -> bool:
        """
        Guarda en base de datos el registro de una tienda.
        """
        self.add(STORE_TABLE, store.get_store_obj())
    
    def find_store(self, query: dict=None):
        """
        Devuelve registros de tiendas de la base de datos según una consulta.
        """
        return self.get(table=STORE_TABLE, query=query)
    
    def add_item(self, item: MC_Item) -> bool:
        """
        Guarda en base de datos el registro de un item.
        """
        self.add(ITEM_TABLE, item.get_item_obj())
    
    def find_item(self, query: dict=None):
        """
        Devuelve un único items de la base de datos según una consulta. En caso de existir más de uno, devuelve el primero. Devuelve None si no existe.
        """
        items = self.get(table=ITEM_TABLE, query=query)
        if items:
            return items[0]
        else:
            return None
    
    def find_items(self, query: dict=None):
        """
        Devuelve registros de items de la base de datos según una consulta.
        """
        return self.get(table=ITEM_TABLE, query=query)
    
    def update_items(self, items: list[MC_Item]):
        """
        Actualiza todos los items de la lista con la información que contienen.
        """
        for item in items:
            return self.update(table=ITEM_TABLE, query={"item_id" : item.get_id()}, new_values=item.get_item_obj())
    
    def add_ticket(self, ticket: Ticket) -> bool:
        """
        Guarda en base de datos el registro de un ticket.
        """
        self.add(TICKET_TABLE, ticket.get_ticket_obj())
    
    def find_tickets(self, query: dict=None):
        """
        Devuelve registros de tickets de la base de datos según una consulta.
        """
        return self.get(table=TICKET_TABLE, query=query)
    
    def tickets_btween_dates(self, date_1: datetime, date_2: datetime) -> list[Ticket]:
        """
        Devuelve todos los tickets realizados entre dos fechas, ambas incluídas.
        """
        date_1, date_2 = min(date_1, date_2), max(date_1, date_2)
        res = []

        all_tickets = self.find_tickets()
        for ticket in all_tickets:
            ticket_obj = Ticket(
                ticket_id=ticket["id"],
                customer=ticket["customer"],
                store_name=ticket["store_name"],
                items=ticket["items"],
                date=datetime.fromisoformat(ticket["date"]),
                details=ticket["details"],
                money_symbology=ticket["money_symbology"],
            )

            if ticket_obj.get_date() >= date_1 and ticket_obj.get_date() <= date_2:
                res.append(ticket_obj)

        return res

    def get_cathegories(self, query: dict = None):
        """
        Devuelve las categorías de base de datos.
        """
        return self.get(table=CATHEGORIES_TABLE, query=query)

    def add_cathegory(self, new_cathegory: str):
        """
        Añade una nueva categoría a la base de datos.
        """
        if not self.get_cathegories(query={"name" : new_cathegory}):
            return self.add(table=CATHEGORIES_TABLE, document={"name" : new_cathegory})
        
        return False

    def del_cathegory(self, cathegory_name: str):
        """
        Elimina una categoría de la base de datos.
        """
        return self.delete(table=CATHEGORIES_TABLE, query={"name" : cathegory_name})

    def upd_cathegory(self, old_cathegory_name: str, new_cathegory_name: str):
        """
        Actualiza una categoría de la base de datos.
        """
        return self.update(table=CATHEGORIES_TABLE, query={"name" : old_cathegory_name}, new_values={"name" : new_cathegory_name})