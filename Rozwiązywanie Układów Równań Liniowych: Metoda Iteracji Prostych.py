import math

e = float(input("Podaj dokładność: "))

tab = [[3,1,2,5],
       [1,-4,1,-7],
       [1,2,3,2]]

wiersze = len(tab)
kolumny = len(tab[0]) - 1
iteracje = 0

tabX = [0 for i in range(wiersze)]
kolejnytabX = [0 for i in range(wiersze)]
dzielniki = [0 for i in range(wiersze)]

for i in range(wiersze):
    dzielniki[i] = tab[i][i]

for i in range(wiersze):
    for j in range(kolumny + 1):
        tab[i][j] = tab[i][j] / dzielniki[i]
    tab[i][i] = 0

for i in range(wiersze):
    for j in range(kolumny):
        tab[i][j] *= -1

def petla():
    global iteracje
    iteracje += 1
    warunek = 3

    for i in range(wiersze):
        nowaWartosc = 0
        for j in range(kolumny + 1):
            if(j != kolumny): nowaWartosc += tab[i][j] * kolejnytabX[j]
            else: nowaWartosc += tab[i][j]
        kolejnytabX[i] = nowaWartosc
        if(abs(kolejnytabX[i] - tabX[i]) < e): warunek -= 1

    if(warunek == 0):
        print("Rozwiązania to:")
        for i in range(wiersze):
            print(kolejnytabX[i])
        print("Iteracje:",iteracje)
    else:
        for i in range(wiersze):
            tabX[i] = kolejnytabX[i]
        petla()

petla()
