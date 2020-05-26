import math
from sympy import *

x = Symbol("x")

y = 3 * (x ** 2) + (20 * x) + 9
y_prim = y.diff(x)
y_bis = y_prim.diff(x)

def funkcja(zmienna, poch):
    if(poch==0): return y.subs({x: zmienna}).evalf()
    elif(poch==1): return y_prim.subs({x: zmienna}).evalf()
    elif(poch==2): return y_bis.subs({x: zmienna}).evalf()

a = float(input("Podaj początek przedziału: "))
b = float(input("Podaj koniec przedziału: "))
e = float(input("Podaj dokładność: "))

iteracje = 1

def sieczne():
    global x0, x1, iteracje
    def petlaA():
        global x0, x1, iteracje
        x1 = x0 - (funkcja(x0, 0)/(funkcja(x0, 0) - funkcja(a, 0))) * (x0 - a)
        if(abs(funkcja(x1, 0)) >= e or abs((funkcja(x1, 0) - funkcja(x0, 0)) >= e)):
           x0 = x1
           iteracje += 1
           petlaA()

    def petlaB():
        global x0, x1, iteracje
        x1 = x0 - (funkcja(x0, 0)/(funkcja(b, 0) - funkcja(x0, 0))) * (b - x0)
        if(abs(funkcja(x1, 0)) >= e or abs((funkcja(x1, 0) - funkcja(x0, 0))) >= e):
           x0 = x1
           iteracje += 1
           petlaB()

    if(funkcja(a, 0) * funkcja(a, 2) > 0):
        x0 = b
        petlaA()
    elif(funkcja(b, 0) * funkcja(b, 2) >0):
        x0 = a
        petlaB()
    print("Rozwiązanie: ", x1)
    print("f(x): ", funkcja(x1, 0))
    print("Liczba iteracji: ", iteracje)


if(funkcja(a, 0) * funkcja(b, 0) < 0): sieczne()
else: print("Warunek konieczny nie został spełniony!")
