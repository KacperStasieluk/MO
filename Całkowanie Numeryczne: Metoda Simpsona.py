import math

def funkcja(x):
    return (1.4*x+0.3)/(2.3 + math.cos((0.4 * x**2) + 1)) 

poczatek_p = float(input("Wartosc poczatkowa przedzialu: "))
koniec_p = float(input("Wartosc koncowa przedzialu: "))

n = int(input("Podaj N: "))

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
    wartosc += funkcja(punkty[0])
    for i in range(0,n):
        petla1 += funkcja(punktyti[i]) 
    wartosc += 4*petla1
    for i in range(1,n):
        petla2 += funkcja(punkty[i])
    wartosc += 2*petla2
    wartosc += funkcja(punkty[n])
    return (h/3)*wartosc

print(wynik())
