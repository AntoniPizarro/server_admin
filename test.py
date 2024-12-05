from pprint import pprint
from time import time

from service import *
from resources import *


if __name__ == "__main__":
    rcon_1 = RCON(
        server_rcon_ip="161.97.132.162",
        server_rcon_port=33475,
        server_rcon_psw="LHga0WuD",
    )
    
    store_1 = MC_Store(
        name="Tienda Test",
        description="Tienda para realizar pruebas",
        owner="granpepinillo",
        items=[],
        money=0,
        rcon=rcon_1
    )
    
    print(rcon_1.playsound_anywhere("minecraft:entity.ender_dragon.death"))
    #print("=======================================================")
    #print(rcon_1.command_response("/data get block -3565 86 -702"))