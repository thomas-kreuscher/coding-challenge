"""Aufgabe: Implementierung einer Stack-Datenstruktur

Schreiben Sie eine Python-Klasse, die eine einfache Stack-Datenstruktur implementiert. 
Der Stack sollte die folgenden Funktionen unterstützen:

push(item): Fügt ein Element oben auf den Stack hinzu.
pop(): Entfernt und gibt das oberste Element vom Stack zurück.
peek(): Gibt das oberste Element vom Stack zurück, ohne es zu entfernen.
is_empty(): Gibt True zurück, wenn der Stack leer ist, ansonsten False.
size(): Gibt die Anzahl der Elemente im Stack zurück."""


from collections import deque
 
stack = deque()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())  # Ausgabe: 3
print(stack.pop())   # Ausgabe: 3
print(stack.size())  # Ausgabe: 2
print(stack.is_empty())  # Ausgabe: False