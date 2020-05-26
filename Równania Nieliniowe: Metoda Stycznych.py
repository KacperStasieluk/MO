import math
from sympy import *

x = Symbol("x")

y = x ** 2 + x - 5
y_prim = y.diff(x)
y_bis = y_prim.diff(x)

def funkcja(zmienna, poch):
    if(poch==0): return y.subs({x: zmienna}).evalf()
    elif(poch==1): return y_prim.subs({x: zmienna}).evalf()
    elif(poch==2): return y_bis.subs({x: zmienna}).evalf()

a = float(input("Podaj początek przedziału: "))
b = float(input("Podaj koniec przedziału: "))
e = float(input("Podaj dokładność: "))
def styczne():
    global x0, x1
    if(funkcja(a, 0) * funkcja(a, 2) > 0):
        x0 = a
    else: x0 = b
    def petla():
        global x0, x1
        x1 = x0 - (funkcja(x0, 0)/funkcja(x0, 1))
        if(abs(funkcja(x1, 0)) > e or abs(x1 - x0) > e):
            x0 = x1
            petla()
    petla()
    print(x1)

if((funkcja(a, 1) * funkcja(b, 1) >= 0) and (funkcja(a, 2) * funkcja(b, 2) >= 0)):
    print("Warunki zbieżności zostały spełnione!")
else: 
    print("Warunki zbieżności NIE zostały spełnione!")

if(funkcja(a, 0) * funkcja(b, 0) < 0): styczne()
else: print("Warunek konieczny nie został spełniony!")
