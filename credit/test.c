#include<stdio.h>
#include<cs50.h>

int main(void)
{
    long cc = get_long("Number: ");
    long copy = cc;

    while (copy >= 100)
        copy /= 10;


    printf ("%li", copy);

}