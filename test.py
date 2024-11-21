from pprint import pprint
from time import time
from datetime import datetime

from service import *
from resources import *

def time_stamp(date_time_format: datetime):
    return f"[{str(date_time_format.date()).replace('-', '/')} {date_time_format.time().hour}:{date_time_format.time().minute}:{date_time_format.time().second}]"

if __name__ == "__main__":
    text = "Hola, esto es una prueba para asegurarnos de que los textos se ciñen a un ancho concreto de caracteres por línea."
    generate_written_book("Pepinillo", text)