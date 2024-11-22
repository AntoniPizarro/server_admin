from .minecraft_content import CHAR_WIDTH, DEFAULT_CHAR_WIDTH

def generate_written_book(author: str, title: str, text: str):
    """
    Filas: 14 por página.
    Píxeles: 114 por fila.

    EJ:
        minecraft:written_book{resolved:true,generation:0,author:"<autor>",title:"",pages:['[[""]],[[""]]']}
    """
    def get_pixels(text: str):
        """
        Devuelve los píxeles que ocupa un texto. Se tienen en cuenta la separación entre caracteres.
        """
        pixels = 0
        for char in text:
            if ord(char) not in CHAR_WIDTH:
                pixels += DEFAULT_CHAR_WIDTH + 1
            else:
                pixels += CHAR_WIDTH[ord(char)] + 1
        
        if pixels > 0:
            pixels -= 1
        
        return pixels

    # Constantes para las dimensiones
    MAX_PIXELS = 114
    MAX_ROWS = 14

    # Variables
    rows = []
    row_words = []
    pixels = 0

    # Recorremos cada palabra y calculamos el ancho que miden
    for word in text.split():
        # Calculamos cuanto ocupa la palabra
        pixels += get_pixels(word)

        # Nos aseguramos de que seguimos estando dentro del margen
        if pixels + get_pixels(" ") < MAX_PIXELS:
            pixels += get_pixels(" ")
            row_words.append(word)
        # En caso contrario creamos la fila y empezamos la siguiente
        else:
            rows.append(row_words.copy())
            row_words = [word]
            pixels = get_pixels(word)

            if pixels + get_pixels(" ") < MAX_PIXELS:
                pixels += get_pixels(" ")
    
    # Añadimos las palabras de la última fila
    rows.append(row_words.copy())
    pages = []
    # Mientras haya más filas que el máximo pormitido por fila, generamos una página nueva
    while len(rows) / MAX_ROWS > 1:
        pages.append(rows[:MAX_ROWS].copy())
        rows = rows[MAX_ROWS:]
    pages.append(rows.copy())

    # Acabamos dando formato a las páginas
    new_pages = []
    for page in pages:
        new_page = []
        for row in page:
            new_page.append(" ".join(row))
        new_pages.append(new_page.copy())
    
    pages_json_text = f"['{str([page for page in new_pages]).replace("'", "\"")}']"

    return "minecraft:written_book{resolved:true,generation:0,author:\"" + author + "\",title:\"" + title + "\",pages:" + pages_json_text + "}"
