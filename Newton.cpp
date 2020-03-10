#include <iostream>

int main()
{
    const int ELEMENTY = 5;
    int x = 1;

    int tabX[ELEMENTY] = {0, 2, 3, 4, 6};
    int tabY[ELEMENTY] = {1, 3, 2, 5, 7};
    double I_rz[ELEMENTY-1];
    double II_rz[ELEMENTY-2];
    double III_rz[ELEMENTY-3];
    double IV_rz;

    for(int j = 0; j < ELEMENTY; j++)
    {
        if(j == 0)
        {
            for(int i = 0; i < ELEMENTY-1; i++)
            {
                I_rz[i] = (tabY[i+1]-tabY[i])/(tabX[i+1]-tabX[i]);
            }
        }
        else if(j == 1)
        {
            for(int i = 0; i < ELEMENTY-2; i++)
            {
                II_rz[i] = (I_rz[i+1]-I_rz[i])/(tabX[i+2]-tabX[i]);
            }
        }
        else if(j == 2)
        {
            for(int i = 0; i < ELEMENTY-3; i++)
            {
                III_rz[i] = (II_rz[i+1]-II_rz[i])/(tabX[i+3]-tabX[i]);
            }
        }
        else if(j == 3)
        {
            IV_rz = (III_rz[1]-III_rz[0])/(tabX[4]-tabX[0]);
        }
    }

    if(ELEMENTY == 2) std::cout << tabY[0] + I_rz[0]*(x-tabX[0]) << std::endl;
    else if(ELEMENTY == 3) std::cout << tabY[0] + I_rz[0]*(x-tabX[0])+II_rz[0]*(x-tabX[0])*(x-tabX[1]) << std::endl;
    else if(ELEMENTY == 4) std::cout << tabY[0] + I_rz[0]*(x-tabX[0])+II_rz[0]*(x-tabX[0])*(x-tabX[1])+III_rz[0]*(x-tabX[0])*(x-tabX[1])*(x-tabX[2])<< std::endl;
    else if(ELEMENTY == 5) std::cout << tabY[0] + I_rz[0]*(x-tabX[0])+II_rz[0]*(x-tabX[0])*(x-tabX[1])+III_rz[0]*(x-tabX[0])*(x-tabX[1])*(x-tabX[2])+IV_rz*(x-tabX[0])*(x-tabX[1])*(x-tabX[2])*(x-tabX[3]) << std::endl;

    //WYNIKI:
/*
    for(int i = 0; i < ELEMENTY-1; i++)
    {
        std::cout << I_rz[i] << std::endl;
    }

    std::cout << std::endl;

    for(int i = 0; i < ELEMENTY-2; i++)
    {
        std::cout << II_rz[i] << std::endl;
    }

    std::cout << std::endl;

    for(int i = 0; i < ELEMENTY-3; i++)
    {
        std::cout << III_rz[i] << std::endl;
    }

    std::cout << std::endl;

    std::cout << IV_rz << std::endl;

*/
    return 0;
}