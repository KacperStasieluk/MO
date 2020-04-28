import math

def funkcja(x):
    return (1.4*x+0.3)/(2.3 + math.cos((0.4 * x**2) + 1)) 

poczatek_p = float(input("Wartosc poczatkowa przedzialu: "))
koniec_p = float(input("Wartosc koncowa przedzialu: "))

n = int(input("Podaj N: "))

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

print(wynik())
