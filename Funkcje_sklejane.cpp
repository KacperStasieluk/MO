#include <iostream>
#include <math.h>

int main()
{
    const int ELEMENTY = 4;
    int tabX[ELEMENTY] = { 1, 3, 5, 7 };
    int tabY[ELEMENTY] = { 1, 8, 9, 17 };
    int uklad[2 * ELEMENTY - 1][2 * ELEMENTY - 1];
    int pochodna1 = 1;
    int pochodna2 = 1;

    for (int i = 0; i < 2 * ELEMENTY - 2; i++)
    {
        for (int j = 0; j < 2 * ELEMENTY - 1; j++)
        {
            uklad[i][j] = 0;
        }
    }

    for (int i = 0; i < ELEMENTY; i++)
    {
        for (int j = 0; j < 2 * ELEMENTY - 2; j++)
        {
            if (j == 0) uklad[i][j] = 1;
            else if (j == 1) uklad[i][j] = tabX[i];
            else if (j == 2) uklad[i][j] = pow(tabX[i], 2);
            else if (j == 3) uklad[i][j] = pow(tabX[i], 3);
            else if ((j == 4) && (i > 0)) uklad[i][j] = pow((tabX[i] - tabX[1]), 3);
            else if ((j == 5) && (i > 1)) uklad[i][j] = pow((tabX[i] - tabX[2]), 3);
            else if ((j == 6) && (i > 2)) uklad[i][j] = pow((tabX[i] - tabX[3]), 3);
        }
        uklad[i][2 * ELEMENTY - 2] = tabY[i];
    }

    for (int j = 0; j < 2 * ELEMENTY - 2; j++)
    {
        if (j == 0) uklad[ELEMENTY][j] = 0;
        else if (j == 1) uklad[ELEMENTY][j] = 1;
        else if (j == 2) uklad[ELEMENTY][j] = 2 * tabX[0];
        else if (j == 3) uklad[ELEMENTY][j] = 3 * tabX[0];
        else if (j == 4) uklad[ELEMENTY][j] = 0;
        else if (j == 5) uklad[ELEMENTY][j] = 0;
        else if (j == 6) uklad[ELEMENTY][j] = 0;
    }
    uklad[2 * ELEMENTY - 4][2 * ELEMENTY - 2] = pochodna1;

    for (int j = 0; j < 2 * ELEMENTY - 2; j++)
    {
        if (j == 0) uklad[ELEMENTY + 1][j] = 0;
        else if (j == 1) uklad[ELEMENTY + 1][j] = 1;
        else if (j == 2) uklad[ELEMENTY + 1][j] = 2 * tabX[ELEMENTY - 1];
        else if (j == 3) uklad[ELEMENTY + 1][j] = 3 * pow(tabX[ELEMENTY - 1], 2);
        else if (j == 4) uklad[ELEMENTY + 1][j] = 3 * pow((tabX[ELEMENTY - 1] - tabX[1]), 2);
        else if (j == 5) uklad[ELEMENTY + 1][j] = 3 * pow((tabX[ELEMENTY - 1] - tabX[2]), 2);
        else if (j == 6) uklad[ELEMENTY + 1][j] = 3 * pow((tabX[ELEMENTY - 1] - tabX[3]), 2);
    }
    uklad[2 * ELEMENTY - 3][2 * ELEMENTY - 2] = pochodna1;

    for (int i = 0; i < 2 * ELEMENTY - 2; i++)
    {
        for (int j = 0; j < 2 * ELEMENTY - 1; j++)
        {
            printf("%5d", uklad[i][j]);
        }
        std::cout << std::endl;
    }
}
