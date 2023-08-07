task = """Aufgabe: Finden der Häufigkeit von Wörtern in einem Text
Schreiben Sie eine Python-Funktion, die einen Text als Eingabe 
erhält und eine Wörterbuch-ähnliche Struktur zurückgibt, in der 
die Wörter des Textes als Schlüssel und ihre jeweilige Häufigkeit 
als Werte dargestellt werden. Die Funktion sollte alle Zeichen 
außer Buchstaben und Zahlen ignorieren und die Wörter sollten 
in Kleinbuchstaben umgewandelt werden, um die Groß-/Kleinschreibung 
zu ignorieren."""

import logging


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def create_dict(x):
    """
    Args: x = string
    """
    logger.info(task)
    x = x.replace(',', ' ').replace('.',' ')
    lower_text = x.lower().split()
    text_dict = {}

    for i in lower_text:
       count = 0
       for j in lower_text:
          if i == j:
             count += 1
             text_dict.update({i:count})
          else:
             pass
    return text_dict



text = "Dies ist ein Text Ein einfacher Text, um die Aufgabe zu lösen."

print(create_dict(text))
