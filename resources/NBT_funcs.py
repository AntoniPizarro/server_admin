def test_print(to_print, title=""):
    '''
    Salida por consola para pruebas.
    '''
    print(f"   ---------   {title}   ---------   \n")
    print(to_print)

def remove_whites(text: str):
    '''
    Elimina los espacios en blanco innecesarios.
    '''
    # Variable para comprobar si estamos en una cadena
    in_string = False

    # Recorremos el texto caracter a caracter
    res = ""
    for char in text:
        # Si el caracter son comillas, alternamos si estamos en una cadena
        if char == "\"":
            in_string = not in_string
        
        # Filtramos todos los espacios en blanco que no sean de una cadena
        if char not in [" ", "\n"] or in_string:
            res += char
    
    return res

def get_content_lvl(text: str, enter_label: str, exit_label: str):
    '''
    Devuelve el primer contenedor que coincida con las etiquetas de apertura y cierre.
    '''
    # Partimos de la primera etiqueta
    res = text[text.find(enter_label):]

    # Variables necesarias
    actual_lvl = 0
    in_string = False
    actual_pos = 0
    finit_pos = len(res) - 1

    # Recorremos el texto caracter a caracter
    for char in res:
        # Comprobamos que no cerramos en un punto intermedio del contenedor con los niveles
        if char == enter_label and actual_pos > 0 and not in_string:
            actual_lvl += 1
            actual_pos += 1
            continue
        elif char == exit_label and actual_pos > 0 and actual_lvl > 0 and not in_string:
            actual_lvl -= 1
            actual_pos += 1
            continue

        # Nos aseguramos de si hemos entrado en una cadena
        if char == "\"" or char == "'":
            in_string = not in_string
        
        # Comprueba que hemos llegado al final del contenedor y paramos el bucle
        if char == exit_label and not in_string and actual_lvl == 0:
            # Calcula la posición en la que acaba el contenedor
            finit_pos = actual_pos + 1
            break
        
        # Por cada caracter, avanzamos una posición
        actual_pos += 1

    # Si por lo que sea, ha habido un problema calculando los niveles, devolvemos datos vacíos
    if actual_lvl != 0:
        return ""

    # Devolvemos hasta la última posición calculada
    return res[:finit_pos]

def nbt_to_list(nbt_text: str):
    '''
    Conversa un NBT en una lista de python.
    '''
    if not nbt_text or nbt_text[0] != "[" or nbt_text[-1] != "]":
        return []

    nbt_text = remove_whites(nbt_text)

    res = []
    comodin = []
    actual_item = ""
    actual_lvl = 0
    in_string = False
    last_string_char = ""
    for char in nbt_text[1:-1]:
        # Nos aseguramos de si hemos entrado en una cadena
        if char in ["\"", "'"]:
            if not in_string:
                last_string_char = char
            
            if char == last_string_char:
                in_string = not in_string

            if not in_string:
                last_string_char = ""
        
        # Comprobamos el nivel en el que nos encontramos
        if char in ["{", "["] and not in_string:
            actual_lvl += 1
        elif char in ["}", "]"] and not in_string:
            actual_lvl -= 1
        
        if ((char != "," or not in_string) and actual_lvl != 0) or in_string:
            actual_item += char
        else:
            if char != ",":
                actual_item += char
            if actual_item:
                comodin.append(actual_item)
            actual_item = ""
        
    comodin.append(actual_item)
    for item in comodin:
        if item:
            if item[0] == "[":
                res.append(nbt_to_list(item))
            elif item[0] == "{":
                res.append(nbt_to_dict(item))
            else:
                res.append(item)
    
    return res

def nbt_to_dict(nbt_text):
    '''
    Conversa un NBT en un diccionario de python.
    '''
    # Comprobaciones previas al proceso
    if type(nbt_text) == dict:
        return nbt_text
    elif not nbt_text or nbt_text[0] != "{" or nbt_text[-1] != "}":
        return {}

    nbt_text = remove_whites(nbt_text)

    # Variables necesarias
    res = {}
    actual_lvl = 0
    actual_key_value = ""
    in_string = False
    last_string_char = ""

    # Iteramos caracter a caracter el contenido de las claves
    for char in nbt_text[1:-1]:
        # Nos aseguramos de si hemos entrado en una cadena
        if char in ["\"", "'"] and char == last_string_char:
            in_string = not in_string
            
            if in_string:
                last_string_char = ""
        
        # Comprobamos el nivel en el que nos encontramos
        if char in ["{", "["] and not in_string:
            actual_lvl += 1
        elif char in ["}", "]"] and not in_string:
            actual_lvl -= 1
        
        # TEST
        if "Lore".lower() in actual_key_value.lower()[:len("lore")]:
            pass

        if char == "," and not in_string and actual_lvl == 0:
            key = actual_key_value[:actual_key_value.find(":")]
            value = actual_key_value[actual_key_value.find(":") + 1:]
            res[key] = value
            actual_key_value = ""
        else:
            actual_key_value += char
    
    if actual_key_value and ":" in actual_key_value:
        key = actual_key_value[:actual_key_value.find(":")]
        value = actual_key_value[actual_key_value.find(":") + 1:]
        res[key] = value

    for key, value in res.items():
        if value:
            if value[0] == "[":
                res[key] = nbt_to_list(value)
            elif value[0] == "{":
                res[key] = nbt_to_dict(value)
    
    return res

def get_file_content(file_path, encoding="utf-8"):
    '''
    Devuelve el contenido de un archivo.
    '''
    res = open(file_path, "r", encoding=encoding).read()
    
    return res

def list_to_nbt(list_obj: list):
    '''
    Conversa una lista de python en un NBT.
    '''
    res = "["
    for item in list_obj:
        if type(item) == list:
            res += f"{list_to_nbt(item)},"
        if type(item) == dict:
            res += f"{dict_to_nbt(item)},"
        else:
            res += f"{item},"
            
    res += "]"

    return res

def dict_to_nbt(dict_obj: dict):
    '''
    Conversa un diccionario de python en un NBT.
    '''    
    res = "{"
    for key, value in dict_obj.items():
        if type(value) == dict:
            res += f"{key}: {dict_to_nbt(value)},"
        elif type(value) == list:
            res += f"{key}: {list_to_nbt(value)},"
        else:
            res += f"{key}: {value},"
    
    res += "}"

    return res

class NBT:
    def __init__(self, nbt_text: str, name: str) -> None:
        if remove_whites(nbt_text)[0] == "[":
            self.nbt = nbt_to_list(remove_whites(nbt_text))
        elif remove_whites(nbt_text)[0] == "{":
            self.nbt = nbt_to_dict(remove_whites(nbt_text))
        else:
            self.nbt = nbt_to_dict("{" + remove_whites(nbt_text) + "}")
        
        self.name = name
    
    def get_name(self):
        return self.name

    def get(self):
        return dict_to_nbt(self.nbt)

    def add(self, attribute, value):
        self.nbt[attribute] = value
    
    def update(self, attribute, value):
        self.add(attribute, value)

class Item_Tag:
    def __init__(self) -> None:
        pass

class Item:
    def __init__(self, item_id: str, count: int, tag: Item_Tag=None) -> None:
        self.item_id = item_id
        self.count = count
        self.tag = tag
    
    def get_item_id(self):
        return self.item_id
    
    def set_item_id(self, new_item_id):
        self.item_id = new_item_id
    
    def get_count(self):
        return self.count
    
    def set_count(self, new_count):
        self.count = new_count
    
    def give(self, added: int=1):
        self.set_count(self.get_count() + added)
    
    def drop(self, droped: int=1):
        self.set_count(self.get_count() - droped)
    
    def get_tag(self):
        return self.tag
    
    def set_tag(self, new_tag):
        self.tag = new_tag
    
    def add_tag_data(self, attribute, value):
        self.tag.add(attribute, value)

class Slot:
    def __init__(self, slot_id: int, item: Item) -> None:
        self.slot_id = slot_id
        self.item = item
    
    def get_slot_id(self):
        return self.slot_id
    
    def set_slot_id(self, new_slot_id):
        self.slot_id = new_slot_id
    
    def get_item(self):
        return self.item
    
    def set_item(self, new_item):
        self.item = new_item
    
    def get(self):
        res = {
            "Slot" : f"{self.get_slot_id()}b",
            "id" : f"\"{self.item.get_item_id()}\"",
            "Count" : f"{self.item.get_count()}b"
        }

        if self.item.get_tag():
            res["tag"] = self.item.get_tag().get()

        return res

class Enchantment:
    def __init__(self, lvl: int, enchantment_id: str) -> None:
        self.lvl = lvl
        self.enchantment_id = enchantment_id
    
    def get_lvl(self):
        return self.lvl
    
    def set_lvl(self, new_lvl):
        self.lvl = new_lvl
    
    def add_lvl(self, lvls=1):
        self.set_lvl(self.get_lvl() + lvls)
    
    def drop_lvl(self, lvls=1):
        if self.get_lvl() - lvls > 0:
            self.set_lvl(self.get_lvl() - lvls)
        else:
            self.set_lvl(1)
    
    def get_enchantment_id(self):
        return self.enchantment_id
    
    def set_enchantment_id(self, new_enchantment_id):
        self.enchantment_id = new_enchantment_id
    
    def get(self):
        res = {
            "lvl" : f"{self.get_lvl()}s",
            "id" : f"{self.get_enchantment_id()}"
        }

        return res
    
    def nbt(self):
        return dict_to_nbt(self.get())

class Enchantments:
    def __init__(self, enchantments: list[Enchantment]) -> None:
        self.enchantments = enchantments
    
    def get_enchantments(self):
        return self.enchantments
    
    def add_enchantment(self, new_enchantment: Enchantment):
        if new_enchantment not in self.get_enchantments():
            self.enchantments.append(new_enchantment)
    
    def del_enchantment(self, enchantment_id):
        for enchantment in self.get_enchantments():
            if enchantment.get_enchantment_id() == enchantment_id:
                self.enchantments.remove(enchantment)
    
    def get(self):
        res = {"Enchantments" : []}
        for enchantment in self.get_enchantments():
            res["Enchantments"].append(enchantment.get())
        
        return res

    def nbt(self):
        return list_to_nbt(self.get())
