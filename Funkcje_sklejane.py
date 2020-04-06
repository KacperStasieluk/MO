import numpy as np

ELEMENTY = 5
tabX = [-4,-2,0,2,4]
tabY = [354,24,-2,-12,90]
uklad = [[0 for y in range(ELEMENTY+2)] for x in range(ELEMENTY+2)]
wyniki = [0 for x in range(ELEMENTY+2)]
pochodna1 = -337
pochodna2 = 143

for x in range(ELEMENTY+2):
    for y in range(ELEMENTY+2):
        uklad[x][y] = 0

for x in range(ELEMENTY):
    for y in range(ELEMENTY+2):
        if y==0: uklad[x][y] = 1
        elif y==1: uklad[x][y] = tabX[x]
        elif y==2: uklad[x][y] = pow(tabX[x],2)
        elif y==3: uklad[x][y] = pow(tabX[x],3)
        elif y==4 and x>0: uklad[x][y] = pow((tabX[x]-tabX[1]),3)
        elif y==5 and x>1: uklad[x][y] = pow((tabX[x]-tabX[2]),3)
        elif y==6 and x>2: uklad[x][y] = pow((tabX[x]-tabX[3]),3)
    wyniki[x] = tabY[x]

for x in range(ELEMENTY+2):
    if x==0: uklad[ELEMENTY][x] = 0
    elif x==1: uklad[ELEMENTY][x] = 1
    elif x==2: uklad[ELEMENTY][x] = 2*tabX[0]
    elif x==3: uklad[ELEMENTY][x] = 3*tabX[0]
    elif x==4: uklad[ELEMENTY][x] = 0
    elif x==5: uklad[ELEMENTY][x] = 0
    elif x==6: uklad[ELEMENTY][x] = 0
wyniki[ELEMENTY] = pochodna1

for x in range(ELEMENTY+2):
    if x==0: uklad[ELEMENTY+1][x] = 0
    elif x==1: uklad[ELEMENTY+1][x] = 1
    elif x==2: uklad[ELEMENTY+1][x] = 2*tabX[ELEMENTY-1]
    elif x==3: uklad[ELEMENTY+1][x] = 3*pow(tabX[ELEMENTY-1],2)
    elif x==4: uklad[ELEMENTY+1][x] = 3*pow((tabX[ELEMENTY-1]-tabX[1]),2)
    elif x==5: uklad[ELEMENTY+1][x] = 3*pow((tabX[ELEMENTY-1]-tabX[2]),2)
    elif x==6: uklad[ELEMENTY+1][x] = 3*pow((tabX[ELEMENTY-1]-tabX[3]),2)
wyniki[ELEMENTY+1] = pochodna2

print(np.matrix(uklad))
print()

print(np.matrix(wyniki))
print()

Z = np.linalg.solve(np.array(uklad), np.array(wyniki))
print(np.matrix(Z))

def Wielomian(x):
    print()
    print("Wynik dla X =",x,":")
    if tabX[0]<=x<tabX[1]: print(Z[0]+(Z[1]*x)+(Z[2]*x*x)+(Z[3]*x*x*x))
    elif tabX[1]<=x<tabX[2]: print(Z[0]+(Z[1]*x)+(Z[2]*x*x)+(Z[3]*x*x*x)+(Z[4]*pow(x-tabX[1], 3)))
    elif tabX[2]<=x<tabX[3]: print(Z[0]+(Z[1]*x)+(Z[2]*x*x)+(Z[3]*x*x*x)+(Z[4]*pow(x-tabX[1], 3))+(Z[5]*pow(x-tabX[2], 3)))
    elif tabX[3]<=x<=tabX[4]: print(Z[0]+(Z[1]*x)+(Z[2]*x*x)+(Z[3]*x*x*x)+(Z[4]*pow(x-tabX[1], 3))+(Z[5]*pow(x-tabX[2], 3))+(Z[6]*pow(x-tabX[3], 3)))

Wielomian(1)
