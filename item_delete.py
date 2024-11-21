from time import time
from datetime import datetime

from service import *
from resources import minutes_to_seconds, seconds_to_minutes

def time_stamp(date_time_format: datetime):
    return f"[{str(date_time_format.date()).replace('-', '/')} {date_time_format.time().hour}:{date_time_format.time().minute}:{date_time_format.time().second}]"

if __name__ == "__main__":
    rcon_1 = RCON(
        server_rcon_ip="161.97.132.162",
        server_rcon_port=33475,
        server_rcon_psw="LHga0WuD"
    )
    
    time_1 = None
    time_2 = None
    time_3 = None
    ADVISE_1 = 20
    TIME_COUNT_MAX = 5
    time_count = ADVISE_1
    
    SEGUNDOS_CICLO = minutes_to_seconds(1)

    print(f"{time_stamp(datetime.now())} -> START")
    print(rcon_1.kill_items())
    rcon_1.server_msg('[{"text":"Próxima limpieza en "},{"text":"' + str(int(seconds_to_minutes(SEGUNDOS_CICLO))) + ' minutos","color":"yellow"}]')
    while True:
        if time_1 == None:
            time_1 = time()
        
        time_2 = time()
        if time_2 - time_1 >= SEGUNDOS_CICLO - ADVISE_1:
            if time_count == ADVISE_1:
                rcon_1.server_msg('[{"text":"Se van a eliminar los items del suelo en "},{"text":"' + str(time_count) + 's","color":"yellow"}]')
                time_count -= 1
                time_3 = time()
                
            if time_count == TIME_COUNT_MAX:
                rcon_1.server_msg('[{"text":"Se van a eliminar los items del suelo en "},{"text":"' + str(time_count) + 's","color":"yellow"}]')
                time_count -= 1
                time_3 = time()
            
            if time_2 - time_3 >= 1:
                if time_count < TIME_COUNT_MAX:
                    rcon_1.server_msg('[{"text":"' + str(time_count) + 's","color":"yellow"}]')
                time_count -= 1
                time_3 = time()
                
            if time_count < 0:
                time_count = ADVISE_1
                print(f"{time_stamp(datetime.now())} -> DELETES")
                print(rcon_1.kill_items())
                #server_msg("!!No se han eliminado porque estoy haciendo pruebas¡¡")
                rcon_1.server_msg('[{"text":"Próxima limpieza en "},{"text":"' + str(int(seconds_to_minutes(SEGUNDOS_CICLO))) + ' minutos","color":"yellow"}]')
                time_1 = None