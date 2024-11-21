from .db import Data_Base as DB
from .minecraft_store import MC_Item, Ticket, Store

STORE_TABLE = "stores"
ITEM_TABLE = "items"
TICKET_TABLE = "tickets"

class Store_DB(DB):
    def __init__(self, host):
        super().__init__(host)
    
    def add_store(self, store: Store) -> bool:
        """
        Guarda en base de datos el registro de una tienda.
        """
        self.add(STORE_TABLE, store.get_store_obj())
    
    def find_store(self, query: dict):
        """
        Devuelve registros de tiendas de la base de datos según una consulta.
        """
        return self.get(table=STORE_TABLE, query=query)
    
    def add_item(self, item: MC_Item) -> bool:
        """
        Guarda en base de datos el registro de un item.
        """
        self.add(ITEM_TABLE, item.get_item_obj())
    
    def find_items(self, query: dict):
        """
        Devuelve registros de items de la base de datos según una consulta.
        """
        return self.get(table=ITEM_TABLE, query=query)
    
    def add_ticket(self, ticket: Ticket) -> bool:
        """
        Guarda en base de datos el registro de un ticket.
        """
        self.add(TICKET_TABLE, ticket.get_ticket_obj())
    
    def find_tickets(self, query: dict):
        """
        Devuelve registros de tickets de la base de datos según una consulta.
        """
        return self.get(table=TICKET_TABLE, query=query)
    