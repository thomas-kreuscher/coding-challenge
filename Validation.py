"""Aufgabe: Validierung von Klammerausdrücken

Schreiben Sie eine Python-Funktion, die einen String 
als Eingabe erhält und überprüft, ob die darin enthaltenen 
Klammerausdrücke korrekt geschachtelt sind. Die Klammerausdrücke 
bestehen aus runden Klammern "()", eckigen Klammern "[]" und 
geschweiften Klammern "{}". Die Funktion sollte True zurückgeben, 
wenn die Klammerausdrücke korrekt geschachtelt sind, andernfalls False."""


text1 = "((([{}])))"
text2 = "([)]"


def nested_term(text):
      a = int(len(text) / 2)
      # print(a)
      for f, b in zip(text[0:a], reversed(text[-a:])):
        # print(f,b)
        if [f,b] == ['(', ')'] or [f,b] == ['[', ']'] or [f,b] == ['{', '}']:
          print(f,b,True)
        else:
          print(f,b,False)
          # exit()

      


print("This is Text1:")  
a = nested_term(text1)
a

print("This is Text2:") 
nested_term(text2)

