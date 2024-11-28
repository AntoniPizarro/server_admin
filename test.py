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
    
    #print(rcon_1.playsound_anywhere("minecraft:entity.ender_dragon.ambient"))
    print(rcon_1.xp("atlasmmc", 0, "query"))
    print(rcon_1.xp("atlasmmc", 9999, "add", "points"))
    print(rcon_1.xp("atlasmmc", 0, "query"))
    
    print(rcon_1.xp("atlasmmc", 28, "set", "points"))