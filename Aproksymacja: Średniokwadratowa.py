import math
import numpy as np

def oblicz_calke(poczatek_p, koniec_p, potega):
        n = 100

        punkty = [None] * (n+1)
        punktyti = [None] * (n)
        punkty[0] = poczatek_p
        punkty[n] = koniec_p

        for i in range(1,n):
            punkty[i] = poczatek_p + (i/n)*(koniec_p-poczatek_p)

        for i in range(n):
            punktyti[i] = (punkty[i+1] + punkty[i])/2

        h = (punkty[1]-punkty[0])/2

        def wynik():
            wartosc = 0
            petla1 = 0
            petla2 = 0
            wartosc += pow(funkcja_f(punkty[0]), potega)
            for i in range(0,n):
                petla1 += pow(funkcja_f(punktyti[i]), potega) 
            wartosc += 4*petla1
            for i in range(1,n):
                petla2 += pow(funkcja_f(punkty[i]), potega)
            wartosc += 2*petla2
            wartosc += pow(funkcja_f(punkty[n]), potega)
            return (h/3)*wartosc

        return wynik()

def funkcja_bazowa(x, n):
    return x**n

def funkcja_p(x):
    return 1

def funkcja_f(x):
    return math.sqrt(x)

x = 1
a = float(input("Podaj dolna wartosc przedzialu: "))
b = float(input("Podaj gorna wartosc przedzialu: "))
n = int(input("Podaj stopien wielomianu: "))

tablica = [[None for i in range(n+1)] for j in range(n+1)]
wyniki = [None for i in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        tablica[i][j] = funkcja_bazowa(x, i) * funkcja_bazowa(x, j) * funkcja_p(x) * oblicz_calke(a, b, n * (i+j))

for i in range(n+1):
    wyniki[i] = funkcja_bazowa(x, i) * funkcja_f(x) * funkcja_p(x) * oblicz_calke(a, b, n*i+1)

print(np.array(tablica))
print(np.array(wyniki))

Z = np.linalg.solve(np.array(tablica, dtype='float'), np.array(wyniki, dtype='float'))

wartosc = float(input("Podaj wartosc X, dla ktorej obliczasz: "))

suma = 0

for i in range(n+1):
    suma += Z[i]*pow(wartosc, i)

print(suma)
