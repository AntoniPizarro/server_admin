from pprint import pprint
from time import time
from datetime import datetime

from service import *
from resources import *

def time_stamp(date_time_format: datetime):
    return f"[{str(date_time_format.date()).replace('-', '/')} {date_time_format.time().hour}:{date_time_format.time().minute}:{date_time_format.time().second}]"

if __name__ == "__main__":
    width = 20
    pprint([text_row.center(width) for text_row in fill_string("Hola, esto es una prueba para asegurarnos de que los textos se ciñen a un ancho concreto de caracteres por línea.", width)])
    print()
    pprint([text_row.rjust(width) for text_row in fill_string("Hola, esto es una prueba para asegurarnos de que los textos se ciñen a un ancho concreto de caracteres por línea.", width)])
    print()
    pprint([text_row.ljust(width) for text_row in fill_string("Hola, esto es una prueba para asegurarnos de que los textos se ciñen a un ancho concreto de caracteres por línea.", width)])