import math

def calka(j, poczatek_p, koniec_p):
    def funkcja(x):
        return pe() * (wielomian(j, x) ** 2)

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

def calka2(j, poczatek_p, koniec_p):
    def funkcja(x):
        return pe() * wielomian(j, x) * F(x)

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

def pe():
    return 1

def F(x):
    return math.exp(x)

poczatek = float(input("Podaj początek przedziału: "))
koniec = float(input("Podaj koniec przedziału: "))
X = float(input("Podaj X: "))
N = int(input("Podaj N: "))

def wielomian(n, x):
    if(n==0): return 1
    elif(n==1): return x
    else: return (1/n) * ((2 * (n - 1) + 1) * x * wielomian(n-1,x) - ((n-1) * wielomian(n-2,x)))

Lambda = [0 for i in range(N)]
C = [0 for i in range(N)]

for j in range(N):
    Lambda[j] = calka(j, poczatek, koniec)
    C[j] = (1/Lambda[j]) * calka2(j, poczatek, koniec)

wynik = 0
for i in range(N):
    wynik += C[i] * wielomian(i, X)

print(wynik)
