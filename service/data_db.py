from .db import Data_Base as DB
from config import DATA_TABLE, DEFAULT_DATA

class Data_DB(DB):
    def __init__(self, host):
        super().__init__(host)
    
    def get_data(self, data_id: str):
        """
        Devuelve la información de la tienda de la base de datos.
        """
        data = self.get(table=DATA_TABLE, query={"id" : data_id})
        if len(data) > 0:
            data = data[0]
        else:
            data = DEFAULT_DATA

        return {
            "money" : data["money"]
        }

    def save_data(self, data_id: str, money: int):
        """
        Guarda la información en base de datos.
        """
        data_to_save = {
            "money" : money
        }
        
        return self.update(table=DATA_TABLE, query={"id" : data_id}, new_values=data_to_save)