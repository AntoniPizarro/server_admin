from datetime import datetime

def time_stamp(date_time_format: datetime):
    return f"[{str(date_time_format.date()).replace('-', '/')} {date_time_format.time().hour}:{date_time_format.time().minute}:{date_time_format.time().second}]"

def minutes_to_seconds(minutes):
    return minutes * 60

def seconds_to_minutes(seconds):
    return seconds / 60

def fill_string(text: str, width: int) -> list[str]:
    """
    Ajusta un texto a un determinado número de caracteres por línea. Separa por palabras
    """
    res = []
    row = ""
    for word in text.split():
        if len(row + word) > width:
            res.append(row[:-1])
            row = ""
            if len(word) > width:
                while len(word) > width:
                    res.append(word[:width])
                    word = word[10:]
        row += word + " "
    
    res.append(row)
    
    return res