import math
import numpy as np
import random

n = 5

tabX = [-1, -0.5, 0, 0.5, 1]
tabY = [None for i in range(n)]

for i in range(n):
    tabY[i] = math.sqrt(2 * (tabX[i] ** 3) - tabX[i] + 9)

m = int(input("Wprowadz stopien wielomianu: "))

tablica = [[None for i in range(m+1)] for j in range(m+1)]
wyniki = [None for i in range(m+1)]

suma = 0
for k in range(m+1):
    for j in range(m+1):
        for i in range(n):
            suma = suma + tabX[i] ** (k+j)
        tablica[k][j] = suma + random.uniform(0.0000000000000001, 0.00000000000001)
        suma = 0


suma2 = 0
for k in range(m+1):
    for i in range(n):
        suma2 = suma2 + (tabX[i] ** k) * tabY[i]
    wyniki[k] = suma2 + random.uniform(0.0000000000000001, 0.00000000000001)
    suma2 = 0

X = float(input("Podaj X: "))

Z = np.linalg.solve(np.array(tablica, dtype='float'), np.array(wyniki, dtype='float'))

sumaOstateczna = 0
for i in range(m+1):
    sumaOstateczna += Z[i] * (X ** i)

print(sumaOstateczna)
