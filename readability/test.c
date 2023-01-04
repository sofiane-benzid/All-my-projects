#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int count_letters(string txt);
int count_words(string txt);
int count_sentences(string txt);

int main(void)
{
    string text = get_string ("Text: ");
    float words = 1;
    float sentences = 0;
    float L = 0;
    float S = 0;
    int letter = count_letters(text);
    int word = count_words(text);
    int sentence = count_sentences(text);
    L = (float)letter/(float)word*100.0;
    S = (float)sentence/(float)word*100.0;
    float index = 0.0588 * L - 0.296 * S - 15.8;
    if (index < 1)
    {
    printf ("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf ("Grade 16+\n");
    }
    else
    {
        printf ("Grade %f\n",index);
    }
    printf ("%f L %f S\n", L, S);
}


int count_letters(string txt)
{
    float letters = 0;
    for (int i = 0; i < strlen(txt); i++)
    {
        if (isalpha(txt[i]))
        {
            letters++;
        }
    }
    return letters;
}

int count_words(string txt)
{
    int words = 1;
    for (int i = 0; i < strlen(txt); i++)
    {
        if (txt[i] == ' ')
        {
            words++;
        }
    }
    return words;
}

int count_sentences(string txt)
{
    int sentences = 0;
    for (int i = 0; i < strlen(txt); i++)
    {
        if (txt[i] == '.' || txt[i] == '?' || txt[i] == '!')
        {
            sentences++;
        }
    }
    return sentences;
}