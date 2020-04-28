import numpy as np

tabX = []
tabY = []

ilosc_argumentow = int(input("Wprowadz liczbe argumentow: "))

print()

for x in range(ilosc_argumentow):
    argument = int(input("Podaj kolejny X: "))
    tabX.append(argument)

print()

for y in range(ilosc_argumentow):
    wartosc = int(input("Podaj kolejny Y: "))
    tabY.append(wartosc)

print()

pochodna1 = int(input("Wprowadz pierwsza pochodna: "))

print()

pochodna2 = int(input("Wprowadz druga pochodna: "))

print()

uklad = [[0 for y in range(len(tabX)+2)] for x in range(len(tabX)+2)]
wyniki = [0 for x in range(len(tabX)+2)]


for x in range(len(tabX)):
    for y in range(len(tabX)):
        uklad[x][y] = 0

for x in range(len(tabX)):
    for y in range(len(tabX)+2):
        if y==0: uklad[x][y] = 1
        elif y<=3: 
            uklad[x][y] = pow(tabX[x],y)
        elif x>(y-4):
            uklad[x][y] = pow((tabX[x]-tabX[y-3]),3)

    wyniki[x] = tabY[x]

for x in range(len(tabX)+2):
    if x==0: uklad[len(tabX)][x] = 0
    elif x==1: uklad[len(tabX)][x] = 1
    elif x<=3: 
        uklad[len(tabX)][x] = x*tabX[0]
    else: 
        uklad[len(tabX)][x] = 0
wyniki[len(tabX)] = pochodna1

for x in range(len(tabX)+2):
    if x==0: uklad[len(tabX)+1][x] = 0
    elif x==1: uklad[len(tabX)+1][x] = 1
    elif x==2: uklad[len(tabX)+1][x] = 2*tabX[len(tabX)-1]
    elif x==3: uklad[len(tabX)+1][x] = 3*pow(tabX[len(tabX)-1],2)
    else:
        uklad[len(tabX)+1][x] = 3*pow((tabX[len(tabX)-1]-tabX[x-3]),2)
wyniki[len(tabX)+1] = pochodna2

print(np.matrix(uklad))
print()

print(np.matrix(wyniki))
print()

Z = np.linalg.solve(np.array(uklad), np.array(wyniki))
print(np.matrix(Z))

def Wielomian(x):
    mnozaca = 0
    print()
    print("Wynik dla X =",x,":")
    if tabX[0]<=x<tabX[1]: print(Z[0]+(Z[1]*x)+(Z[2]*x*x)+(Z[3]*x*x*x))
    elif tabX[1]<=x<tabX[2]: print(Z[0]+(Z[1]*x)+(Z[2]*x*x)+(Z[3]*x*x*x)+(Z[4]*pow(x-tabX[1], 3)))
    elif tabX[2]<=x<tabX[ilosc_argumentow-1]: 
        for j in range(2, ilosc_argumentow-1):
            mnozaca += (Z[j+2]*pow(x-tabX[j-1], 3))
    print(Z[0]+(Z[1]*x)+(Z[2]*x*x)+(Z[3]*x*x*x) + mnozaca)

Wielomian(int(input("Wprowadz X, dla ktorego obliczasz: ")))
