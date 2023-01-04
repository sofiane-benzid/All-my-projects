#include<stdio.h>
#include<cs50.h>

void CheckSum(long n);

int main(void)
{
    long cc = get_long("Number: ");
    CheckSum(cc);

}

void CheckSum(long n)
{
    long copy = n;
    long copy2= copy;
    long x = 10;
    long y = 1;
    int sum1 = 0;
    int sum2 = 0;
    int sum = 0;
    int holder = 0;
    int holder2= 0;
    int mlt2 = 0;
    int check;
    long n1 = n;
    long n2 = n;
    int len = 0;
    long n3 = n;
    while (copy2 != 0)
    {
        copy2 = copy2/100;

        holder = copy/x % 10;
        holder2 = copy/y % 10;

        x = x * 100;
        y = y * 100;

        mlt2 = holder * 2;

        if (mlt2 >= 10)
        {
            sum1 += (mlt2/10%10) + (mlt2%10);
        }
        else
        {
            sum1 += mlt2;
        }
        sum2 += holder2;

        sum = sum1 + sum2;
    }
    check = sum % 10;

    while(true)
    {
        len++;
        n3 = n3 / 10;
        if (n3 == 0)
            break;
    }

    while (n1 >= 100)
        n1 /= 10;
    while (n2 >= 10)
        n2 /= 10;


    if (check == 0)
        {
            if (len == 15 && ( n1 == 34 || n1 == 37))
            {
                printf("AMEX\n");
            }
            else if (len == 16 && (n1 == 51 || n1 == 52 || n1 == 53 || n1 == 54 || n1 == 55))
            {
                printf("MASTERCARD\n");
            }
            else if ((len == 16 || len == 13) && n2 == 4)
            {
                printf("VISA\n");
            }
            else
                printf ("INVALID\n");

        }
    else
        printf ("INVALID\n");

}

