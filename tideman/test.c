#include <stdio.h>
#include <cs50.h>

int sum(int n, int m);

int main(void)
{
    int n = get_int("Number: ");
    int m = get_int("Number: ");

    int i = sum(n, m);
    printf("%i\n", i);
}

int sum(int n, int m)
{

    if (n == 0)
        return 1;
    else if (m == 0 || n < 0)
        return 0;
    else
        {
        int calc = sum(n - m, m) + sum(n, m - 1);
        return calc;
        }
}