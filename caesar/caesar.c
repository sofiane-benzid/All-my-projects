#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

bool only_digits(string s);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    string notkey = argv[1];
    if (!only_digits(notkey))
    {
        printf("Key must be numerical\n");
        return 1;
    }
    int key = atoi(notkey);
    string text = get_string("plaintext: ");

    char ciphertext[strlen(text) + 1];

    for (int i = 0, c = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            if (isupper(text[i]))
            {
                c = (text[i] - 65 + key) % 26;
                ciphertext[i] = 'A' + c;
            }
            else if (islower(text[i]))
            {
                c = (text[i] - 97 + key) % 26;
                ciphertext[i] = 'a' + c;
            }
        }
        else
            ciphertext[i] = text[i];

    }
    ciphertext[strlen(text)] = '\0';
    printf ("ciphertext: %s", ciphertext);
    printf("\n");
}

bool only_digits(string s)
{
    for (int i =0; i < strlen(s); i++)
    {
        if (! isdigit(s[i]))
            return false;
    }
    return true;
}