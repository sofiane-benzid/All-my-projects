#include<stdio.h>

int main(void)
{
    int Gx[3][3] = {{-1, 0 , 1}, {-2, 0 , 2}, {-1, 0 , 1}};
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("%i\n", Gx[i][j]);
        }
    }
}

