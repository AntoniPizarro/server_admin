from time import time
from datetime import datetime

from service import *

def time_stamp(date_time_format: datetime):
    return f"[{str(date_time_format.date()).replace('-', '/')} {date_time_format.time().hour}:{date_time_format.time().minute}:{date_time_format.time().second}]"

if __name__ == "__main__":
    rcon_1 = RCON(
        server_rcon_ip="161.97.132.162",
        server_rcon_port=33475,
        server_rcon_psw="LHga0WuD"
    )
    
    players = [
        "granpepinillo",
        "LonelyWolf",
        "Raazx9",
        "dncm757",
        "tronlovexx",
        "bimbi",
        "adricaba16"
    ]
    player = players[0]
    items = [
        r'{id:"minecraft:stick",Count:1b,Slot: 0b}',
        r'{id:"minecraft:oak_planks",Count:2b,Slot: 1b}',
    ]
    
    #print(rcon_1.playsound_anywhere("minecraft:entity.wither.spawn"))
    print(rcon_1.falling_chest(player, items))