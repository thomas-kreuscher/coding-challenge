"""Aufgabe: Implementierung einer Stack-Datenstruktur

Schreiben Sie eine Python-Klasse, die eine einfache Stack-Datenstruktur implementiert. 
Der Stack sollte die folgenden Funktionen unterstützen:

push(item): Fügt ein Element oben auf den Stack hinzu.
pop(): Entfernt und gibt das oberste Element vom Stack zurück.
peek(): Gibt das oberste Element vom Stack zurück, ohne es zu entfernen.
is_empty(): Gibt True zurück, wenn der Stack leer ist, ansonsten False.
size(): Gibt die Anzahl der Elemente im Stack zurück."""


class DataStack:
    """
    """

    def __init__(self, stack, items):
        self.stack = stack
        self.items = items
        
    def push(self):
        x = self.stack
        print(x)
        x.append(items)
        print(x)
    
    def pop(self):
        x = self.stack
        x.remove(items)
        print(x)





list = ['a', 'b', 'c']
items = 1

a = DataStack(list, items)
a.push()
a.pop()


