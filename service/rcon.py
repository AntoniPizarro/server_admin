from random import randint

from mctools import RCONClient

from resources import sounds

class RCON:
    def __init__(self, server_rcon_ip: str, server_rcon_port: int, server_rcon_psw: str):
        self.server_rcon_ip = server_rcon_ip
        self.server_rcon_port = server_rcon_port
        self.server_rcon_psw = server_rcon_psw
        self.rcon = RCONClient(self.server_rcon_ip, self.server_rcon_port)
    
    def command_response(self, command: str):
        '''
        Ejecuta un comando en servidor y devuelve una respuesta.
        '''
        res = ""
        
        self.rcon.login(self.server_rcon_psw)
        
        #print(command)
        res = self.rcon.command(command)
        
        self.rcon.stop()
        
        # Formateamos la respuesta para eliminar caracteres
        res = res.replace("\x1b[0m", "")
        res = res.replace("\n", "")
        
        return res
    
    def get_player_inventory(self, player_name: str, slot: int=None):
        '''
        Devuelve la un objeto YAML con los datos del inventario de un jugador.
        '''
        if slot == None:
            res = self.command_response(f"data get entity {player_name} Inventory")
        else:
            res = self.command_response(f"data get entity {player_name} Inventory[{slot}b]")
            
        return res[res.find("entity data: ") + len("entity data: "):]

    def private_msg(self, msg: str, player: str):
        '''
        Envía un mensage privado a un jugador.
        '''
        return self.command_response(f"tellraw {player} {msg}")

    def server_msg(self, msg: str):
        '''
        Muestra un mensage por chat a todos los jugadores.
        '''
        return self.private_msg(msg=msg, player="@a")

    def kill_items(self):
        '''
        Elimina los items del servidor.
        '''
        return self.command_response(f"/kill @e[type=minecraft:item]")

    def give_item(self, player_nickname: str, item: str, ammount: int=1, data: str=""):
        '''
        Da a un jugador uno o varios items.
        '''
        return self.command_response("/give " + player_nickname + " " + item + data + " " + str(ammount))

    def playsound_anywhere(self, sound: str=None):
        '''
        Reproduce un sonido en todos los jugadores.
        
        EJEMPLOS:
            true_ending:music.dragon
            minecraft:entity.wither.spawn
        '''
        # Si no se especifica un sonido, se utiliza uno aleatorio
        if sound == None:
            sound_cathegory = list(sounds.keys())[randint(0, len(sounds.keys()) - 1)]
            sound_source = sounds[sound_cathegory][randint(0, len(sounds[sound_cathegory]) - 1)]
            sound = f"{sound_cathegory}:{sound_source}"
            
        return self.command_response(f"/execute at @a run playsound {sound} voice @a")

    def get_scoreboard(self, sc_name: str, player: str):
        '''
        Devuelve los puntos de un 'scoreboard' que tiene un jugador.
        '''
        res = self.command_response(f"/scoreboard players get {player} {sc_name}")
        if res[:len("Can't get")] == "Can't get":
            return 0
        else:
            value = res[res.find(player) + len(f"{player} has "):res.find(" [")]
            return int(value)

    def effect_player(self, player: str, effect: str, time: int=0, amplifier: int=0):
        '''
        Da un efecto a un jugador. Por defecto el efecto dura por siempre y sin amplificaciones.
        '''
        if time < 1:
            time_value = f"infinite"
        else:
            time_value = f"{time}"
        
        if amplifier > 255:
            amplifier = 255
        elif amplifier < 0:
            amplifier = 0
        
        return self.command_response(f"/effect give {player} {effect} {time_value} {amplifier}")

    def teleport(self, target_1: str, target_2: str):
        '''
        Teletransporta un objetivo a a otro.
        '''
        return self.command_response(f'/tp {target_1} {target_2}')

    def troll_player(self, player: str):
        '''
        Realiza una trolleada a un jugador.
        
        Estaría bién formular varios trolleos diferentes y que la trolleada fuera aleatoria.
        '''
        cmd_1 = self.command_response(f"/effect give {player} minecraft:resistance 15 255 true")
        cmd_2 = self.command_response(f"/tp {player} ~ ~200 ~")
        
        return cmd_1 + "\n\n" + cmd_2

    def supply_chest(self, player: str, items: list=None):
        '''
        Invoca un cofre que cae del cielo con items sobre un jugador.
        '''
        # IMPORTANTE: los items deben especificar el slot o no aparecerá más que el primero.
        if items == None:
            items = []
        
        height = 100
        fireworks_time = (height / 2) * 1.20
        #print(r'/give ' + player + ' minecraft:ender_dragon_spawn_egg{EntityTag:{id:"falling_block",BlockState:{Name:"minecraft:chest"},TileEntityData:{Items:[' + ",".join(items) + ']},DropItem:1,Motion:[0.0d,0.1d,0.0d]}}')
        #return self.command_response(r'/give ' + player + ' minecraft:ender_dragon_spawn_egg{EntityTag:{id:"falling_block",BlockState:{Name:"minecraft:chest"},TileEntityData:{Items:[' + ",".join(items) + ']},DropItem:1,Motion:[0.0d,0.1d,0.0d]}}')
        
        return self.command_response(r'/execute at ' + player + ' run summon falling_block ~ ~1 ~ {BlockState:{Name:"minecraft:chest"},TileEntityData:{Items:[' + ",".join(items) + ']},DropItem:1,Motion:[0.0d,0.1d,0.0d]}')

    def xp(self, target: str, ammount, action: str="add", xp_type: str="points"):
        """
        Añade experiencia a un jugador.
            actions: add, set, query
            xp_type: points, levels
        """
        if action not in ["add", "set", "query"]:
            action = "add"
            
        if xp_type not in ["points", "levels"]:
            xp_type = "points"
        
        command = f"/xp {action} {target}"
        
        if action != "query":
            command += f" {ammount}"
        
        command += f" {xp_type}"
        
        return self.command_response(command)

# IN DEV
def enchant_specific_slot(player_name, slot, enchant_id, lvl):
    '''
    Encanta un objeto en un slot en concreto. Si no existe ese objeto,
    entonces no hace nada, de lo contrario, elimina el objeto y lo devuelve
    con el nuevo encantamiento.
    '''
    #slot = get_player_inventory(player_name, slot)
    #if f"Slot: {slot}b"

def get_player_list(self): # Basar esta función en lo que pone en el archivo 'LISTA DE JUGADORES.txt'
    '''
    Devuelve una lista con los jugadores conectados.
    '''
    response = self.command_response("list")
    
    player_list = response[response.find("players online:") + len("players online:"):].split()
    res = []
    for player in player_list:
        if player.replace("\x1b[0m", ""):
            res.append(player.replace("\x1b[0m", ""))
    
    return res