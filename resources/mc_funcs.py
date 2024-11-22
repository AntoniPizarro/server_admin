from pprint import pprint

from .minecraft_content import CHAR_WIDTH, DEFAULT_CHAR_WIDTH

def generate_written_book(author: str, text: str):
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

    MAX_PIXELS = 114
    MAX_ROWS = 14

    rows = []
    row_words = []
    pixels = 0

    for word in text.split():
        pixels += get_pixels(word)
        if pixels + get_pixels(" ") < MAX_PIXELS:
            pixels += get_pixels(" ")
            row_words.append(word)
        else:
            rows.append(row_words.copy())
            row_words = [word]
            pixels = get_pixels(word)

            if pixels + get_pixels(" ") < MAX_PIXELS:
                pixels += get_pixels(" ")
    
    rows.append(row_words.copy())
    pages = []
    while len(rows) / MAX_ROWS > 1:
        pages.append(rows[:MAX_ROWS].copy())
        rows = rows[MAX_ROWS:]
    pages.append(rows.copy())

    new_pages = []
    for page in pages:
        new_page = []
        for row in page:
            new_page.append(" ".join(row))
        new_pages.append(new_page.copy())
    
    pages = new_pages

    pprint(pages)
    pages_json_text = f"['{str([page for page in pages]).replace("'", "\"")}']"
    return pages_json_text