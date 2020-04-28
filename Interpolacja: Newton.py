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

X = int(input("Wprowadz X, dla ktorego obliczasz: "))

print()

suma = tabY[0]
for i in range(1, ilosc_argumentow):
    mnozaca = 1

    for j in range(ilosc_argumentow - i):
        tabY[j] = (tabY[j+1] - tabY[j]) / (tabX[j+i] - tabX[j])

    for k in range(0,i):
            mnozaca *= X - tabX[k]

    suma += tabY[0] * mnozaca

print(suma)
