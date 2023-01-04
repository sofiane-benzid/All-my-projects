#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height;

    do
    {
        height = get_int("Height: ");
    }
    while (height < 1  || height > 8);

    int n = 0;
    int a = height;

    for (int i = 0; i < height; i++)
    {
        n++;
        a--;
        for (int j =0; j < a; j++)
            printf(" ");

        for (int j =0; j < n; j++)
            printf("#");

        for (int j=0; j < 2;j++)
            printf(" ");
            
        for (int j=0; j < n;j++)
            printf("#");
    }
    printf("\n");
}

