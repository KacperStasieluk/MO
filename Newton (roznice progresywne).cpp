#include <iostream>
#include <math.h>

int main()
{
    const int ELEMENTY = 5;
    double x = 1.0;

    int tabX[ELEMENTY] = { -4, -2, 0, 2, 4};
    int tabY[ELEMENTY] = { 354, 24, -2, -12, 90};
    double I_rz[ELEMENTY - 1];
    double II_rz[ELEMENTY - 2];
    double III_rz[ELEMENTY - 3];
    double IV_rz;
    int h = abs(tabX[1] - tabX[0]);

    for (int j = 0; j < ELEMENTY; j++)
    {
        if (j == 0)
        {
            for (int i = 0; i < ELEMENTY - 1; i++)
            {
                I_rz[i] = tabY[i + 1] - tabY[i];
            }
        }
        else if (j == 1)
        {
            for (int i = 0; i < ELEMENTY - 2; i++)
            {
                II_rz[i] = I_rz[i + 1] - I_rz[i];
            }
        }
        else if (j == 2)
        {
            for (int i = 0; i < ELEMENTY - 3; i++)
            {
                III_rz[i] = II_rz[i + 1] - II_rz[i];
            }
        }
        else if (j == 3)
        {
            IV_rz = III_rz[1] - III_rz[0];
        }
    }

    if (ELEMENTY == 2) std::cout << tabY[0] + ((I_rz[0] / (1 * pow(h, 1))) * (x - 1)) << std::endl;
    else if (ELEMENTY == 3) std::cout << tabY[0] + ((I_rz[0] / (1 * pow(h, 1))) * (x - 1)) + ((II_rz[0] / (2 * pow(h, 2))) * (x - 1) * (x - 2)) << std::endl;
    else if (ELEMENTY == 4) std::cout << tabY[0] + ((I_rz[0] / (1 * pow(h, 1))) * (x - 1)) + ((II_rz[0] / (2 * pow(h, 2))) * (x - 1) * (x - 2)) + ((III_rz[0] / (6 * pow(h, 3))) * (x - 1) * (x - 2) * (x - 3)) << std::endl;
    else if (ELEMENTY == 5) std::cout << tabY[0] + ((I_rz[0] / (1 * pow(h, 1))) * (x - 1)) + ((II_rz[0] / (2 * pow(h, 2))) * (x - 1) * (x - 2)) + ((III_rz[0] / (6 * pow(h, 3))) * (x - 1) * (x - 2) * (x - 3)) + ((IV_rz / (24 * pow(h, 4))) * (x - 1) * (x - 2) * (x - 3) * (x - 4)) << std::endl;

    return 0;
}
