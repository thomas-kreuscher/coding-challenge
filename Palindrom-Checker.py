"""Aufgabe: Palindrom-Checker
Schreiben Sie eine Python-Funktion, die prüft, ob ein 
gegebener String ein Palindrom ist. Ein Palindrom ist 
ein Wort, Satz oder eine Zahl, die rückwärts gelesen 
genauso aussieht wie vorwärts gelesen."""




def is_palindrome(text):
    for (i,j) in zip(text, reversed(text)):
        while i == j:
            return 'Yeah, it´s a palindrome!'
        else:
            return 'Sorry, no palindrome!'



text1 = "radar"
text2 = "python"
text3 = "level"


print(is_palindrome(text1))  # True
print(is_palindrome(text2))  # False
print(is_palindrome(text3))  # True
