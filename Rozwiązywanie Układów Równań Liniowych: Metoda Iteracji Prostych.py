import math

wiersze = int(input("Ile równań podasz? "))
kolumny = int(input("Podaj liczbę współczyników równania: "))
dokladnosc = float(input("Podaj dokładność: "))

tab = [[None] * (kolumny + 1)] * wiersze
tabX = [0 for i in range(wiersze)]
kolejnytabX = [0 for i in range(wiersze)]

for i in range(wiersze ):
    for j in range(kolumny + 1):
        if(j < kolumny): tab[i][j] = int(input("Podaj kolejny współczynnik: "))
        else: tab[i][j] = int(input("Podaj wyraz wolny: "))

for i in range(wiersze):
    for j in range(kolumny + 1):
        tab[i][j] /= tab[i][i]
        if(i == j): tab[i][j] = 0
        if(j != kolumny): tab[i][j] *= -1

def petla():

    warunek = 3
    for i in range(wiersze + 1):

        nowaWartosc = 0
        for j in range(kolumny + 1):
            if(i != j and j != kolumny): tab[i][j] *= kolejnytabX[i]
            nowaWartosc += tab[i][j]
        kolejnytabX[i] = nowaWartosc

        if(abs(kolejnytabX[i] - tabX[i]) < e): warunek -= 1
    if(warunek == 0):
        print("Rozwiązania to:")
        for i in range(wiersze + 1):
            print(kolejnytabX[i])
    else:
        for i in range(wiersze + 1):
            tabX[i] = kolejnytabX[i]
        petla()

petla()
