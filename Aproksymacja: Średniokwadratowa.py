import math
import numpy as np
import random

def calka(ii, jj, poczatek_p, koniec_p):
    def funkcja(x):
        return funkcja_bazowa(x, ii) * funkcja_bazowa(x, jj) * funkcja_p(x)

    n = 100

    h = (koniec_p-poczatek_p)/n

    punkty = [None] * (n+1)
    punkty[0] = poczatek_p
    punkty[n] = koniec_p

    for i in range(1,n):
        punkty[i] = poczatek_p + (i/n)*(koniec_p-poczatek_p)

    def wynik():
        wartosc = 0
        wartosc += funkcja(punkty[0])/2
        for i in range(1,n):
            wartosc += funkcja(punkty[i])
        wartosc += funkcja(punkty[n])/2
        return h*wartosc

    return(wynik())

def calka2(iii, poczatek_p, koniec_p):
    def funkcja(x):
        return funkcja_bazowa(x, iii) * funkcja_f(x) * funkcja_p(x)

    n = 100

    h = (koniec_p-poczatek_p)/n

    punkty = [None] * (n+1)
    punkty[0] = poczatek_p
    punkty[n] = koniec_p

    for i in range(1,n):
        punkty[i] = poczatek_p + (i/n)*(koniec_p-poczatek_p)

    def wynik():
        wartosc = 0
        wartosc += funkcja(punkty[0])/2
        for i in range(1,n):
            wartosc += funkcja(punkty[i])
        wartosc += funkcja(punkty[n])/2
        return h*wartosc

    return(wynik())

def funkcja_bazowa(x, n):
    return x**n

def funkcja_p(x):
    return 1

def funkcja_f(x):
    return math.sqrt(2 * (x**3) - x + 9)

a = float(input("Podaj dolna wartosc przedzialu: "))
b = float(input("Podaj gorna wartosc przedzialu: "))
n = int(input("Podaj stopien wielomianu: "))

tablica = [[0 for i in range(n+1)] for j in range(n+1)]
wyniki = [0 for i in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        tablica[i][j] = calka(i, j, a, b) + random.uniform(0.0000000000000001, 0.00000000000001)

for i in range(n+1):
    wyniki[i] = calka2(i, a, b) + random.uniform(0.0000000000000001, 0.00000000000001)

print(np.array(tablica))
print(np.array(wyniki))

Z = np.linalg.solve(np.array(tablica, dtype='float'), np.array(wyniki, dtype='float'))

wartosc = float(input("Podaj wartosc X, dla ktorej obliczasz: "))

suma = 0

for i in range(n+1):
    suma += Z[i]*pow(wartosc, i)

print(suma)
