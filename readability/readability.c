#include <stdio.h>
#include <string.h>
#include <cs50.h>
#include <ctype.h>
#include <math.h>

float grade (string text);

int main (void)
{
    string text = get_string("Text: ");

    float index = grade(text);

    if (index < 1)
        printf("Before Grade 1\n");
    else if (index >= 16)
        printf ("Grade 16+\n");
    else
        printf ("Grade %i\n", (int)round(index));

}

float grade (string text)
{
    int letters = 0;
    int words = 1;
    int sentences = 0;
    float L, S;
    float index;

    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
            letters++;
        if (text[i] == ' ')
            words++;
         if (text[i] == '.' || text[i] == '?' || text[i] == '!')
            sentences++;
    }
    L = (float)(100.0 * letters) / (float)words;
    S = (float)(100.0 * sentences) / (float)words;

    index = 0.0588 * L - 0.296 * S - 15.8;
    return index;
}