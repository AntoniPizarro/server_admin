from decimal import Decimal, getcontext
from tinydb import TinyDB, Query

class Data_Base:
    
    def __init__(self, host):
        # host hace referencia al directorio en el que se aloja la base de datos de tinydb
        self.db = TinyDB(host)
    
    def get(self, table: str, query: dict=None) -> list:
        if query == None:
            query = {}
        
        try:
            if query:
                result = self.db.table(table).search(Query().fragment(query))
            else:
                result = self.db.table(table).all()
            return result
        except Exception as error:
            print("Ha ocurrido un error: " + str(error))
            return []
    
    def add(self, table: str, document: list | dict) -> bool:
        try:
            inserts = []
            db_table = self.db.table(table)
            if type(document) == dict:
                inserts = db_table.insert(document)
            elif type(document) == list:
                inserts = db_table.insert_multiple(document)
            return inserts != []
        except Exception as error:
            print("Ha ocurrido un error: " + str(error))
            return False
    
    def delete(self, table: str, query: dict) -> bool:
        try:
            return self.db.table(table).remove(Query().fragment(query)) != []
        except Exception as error:
            print("Ha ocurrido un error: " + str(error))
            return False
    
    def update(self, table: str, query: dict, new_values: list | dict):
        try:
            updates = []
            if type(new_values) == dict:
                updates = self.db.table(table).update(new_values, Query().fragment(query))
            elif type(new_values) == list:
                updates = self.db.table(table).update_multiple(new_values, Query().fragment(query))
            return updates != []
        except Exception as error:
            print("Ha ocurrido un error: " + str(error))
            return False
    
    def drop_table(self, table: str):
        self.db.drop_table(table)
    
    @staticmethod
    def same_id_probability(ids_length, chars):
        getcontext().prec = 3
        res = (Decimal(1) / (Decimal(len(chars)) ** Decimal(ids_length))) * Decimal(100)
        return res
    
    @staticmethod
    def check_structure(schema: dict, document: dict, except_keys=[], nullables=[]):
        '''
        Comprueba la estructura y el tipado de un documento con un esquema de referencia.
        '''
        # Creamos una copia del esquema para no alterar el original
        schema_copy = schema.copy()
        # Recorremos las excepciones de claves
        for key in except_keys:
            # Eliminamos aquellas que sean excepciones de comprobación
            if key in schema_copy:
                del schema_copy[key]
            
        # Comprobamos que el documento contenga las claves del esquema
        for key in sorted(schema_copy.keys()):
            if key not in sorted(document.keys()):
                print("Las claves no son las correctas")
                return False
        
        # Recorremos las claves del esquema
        for key in schema_copy.keys():
            # Si el tipo de dato del esquema no coincide con el del documento y el valor no puede ser nulo devuelve False
            if type(schema_copy[key]) != type(document[key]) and schema_copy[key] != type(document[key]) and document[key] == None and key in nullables:
                    print("El tipo de dato de '" + key + "' no es el correcto")
                    return False
            if isinstance(schema_copy[key], dict):
                if not Data_Base.check_structure(schema_copy[key], document[key]):
                    print("El tipo de dato de '" + key + "' no es el correcto")
                    return False
        
        return True