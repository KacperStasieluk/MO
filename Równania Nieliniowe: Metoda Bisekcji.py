import math

def funkcja(x):
    return 3 * (x ** 2) + (20 * x) + 9

a = float(input("Podaj początek przedziału: "))
b = float(input("Podaj koniec przedziału: "))
e = float(input("Podaj dokładność: "))

iteracje = 1

def bisekcja():
    global a, b, e, iteracje
    if(funkcja((a + b)/2) == 0):
        print("Rozwiązanie: ", (a + b)/2)
        print("f(x): ", funkcja((a + b)/2))
        print("Liczba iteracji: ", iteracje)
    elif(funkcja((a + b)/2) * funkcja(a) < 0):
        b = (a + b)/2
    else:
        a = (a + b)/2

    if(abs(funkcja((a + b)/2)) < e):
        print("Rozwiązanie: ", (a + b)/2)
        print("f(x): ", funkcja((a + b)/2))
        print("Liczba iteracji: ", iteracje)
    else:
        iteracje += 1
        bisekcja()

if(funkcja(a) * funkcja(b) < 0): bisekcja()
else: print("Warunek konieczny nie został spełniony!")
