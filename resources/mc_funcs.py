from .minecraft_content import CHAR_WIDTH, DEFAULT_CHAR_WIDTH

def generate_written_book(author: str, text: str):
    """
    Filas: 14 por página.
    Píxeles: 114 por fila.

    EJ:
        minecraft:written_book{resolved:true,generation:0,author:"<autor>",title:"",pages['[[""]],[[""]]']}
    """
    def get_pixels(word: str):
        """
        Devuelve los píxeles que ocupa una palabra. Se tienen en cuenta las separaciones entre letras.
        """
        pixels = 0
        for char in word:
            if ord(char) not in CHAR_WIDTH:
                pixels += DEFAULT_CHAR_WIDTH + 1
            else:
                pixels += CHAR_WIDTH[ord(char)] + 1
        
        if pixels > 0:
            pixels -= 1
        
        return pixels

    MAX_PIXELS = 114
    MAX_ROWS = 14

    rows = []
    row_words = []
    pixels = 0
    
    # Recorreremos el texto palabra por palabra
    for word in text.split():
        # Obtenemos los píxeles que ocupa cada palabra
        pixels += get_pixels(word)
        row_words.append(word)

        if pixels + (len(row_words) - 1) * CHAR_WIDTH[ord(" ")] > MAX_PIXELS:
            new_row = row_words[:-1]
            rows.append(new_row)
            row_words = row_words[-1:]
            pixels = get_pixels(row_words[0])
        
    rows.append(new_row)
    pages = [[] * int(len(rows) / MAX_ROWS)]
    for page in pages:
        while len(page) < MAX_ROWS or not rows:
            print(rows)
            page.append(rows.pop(0))
    
    print("Autor: " + author)
    for page in pages:
        for row in page:
            print(row)