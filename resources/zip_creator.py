import shutil 
import os.path

def generate_comprimed_file(final_name, file_extension, path):
    '''
    Genera un archivo comprimido con el contenido de un directorio concreto.
    params:
        final_name: Nombre del archivo final.
        file_extension: Extensión del archivo comprimido.
        path: Ruta del directorio con el contenido para comprimir.
    '''
    return shutil.make_archive(final_name, file_extension, path)