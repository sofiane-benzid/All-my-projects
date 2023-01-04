#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include <ctype.h>

int main(void)
{
    char *s = get_string("s: ");
    char *t = malloc(3);

    for (int i = 0; i < 4; i++)
    {
        t[i] = s[i];
    }
    t[0] = toupper(t[0]);

    printf("s: %s\n", s);
    printf("t: %s\n", t);
}