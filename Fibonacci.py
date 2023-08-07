"""Aufgabe: Fibonacci-Folge

Schreiben Sie eine Python-Funktion, die die ersten n Elemente 
der Fibonacci-Folge berechnet und als Liste zurückgibt. 
Die Fibonacci-Folge ist eine Sequenz von Zahlen, bei der 
jede Zahl die Summe der beiden vorherigen Zahlen ist, 
wobei die erste Zahl 0 und die zweite Zahl 1 ist."""

# n = 8
# 0 1 2 3 4 5 6 7  --> Stelle
# 0 1 1 2 3 5 8 13 --> Wert

def fibonucci(n):
    if n == 0:
        fib_list =[0]
    else:
            
        fib_list = [0,1]
        for i in range(1,n):
            
            b = fib_list[i] + fib_list[i-1]
            fib_list.append(b)
    
    print(fib_list)

fibonucci(3)