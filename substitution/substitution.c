#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>


int main(int argc, string argv[])
{
    // Key validation

    if (argc != 2)
    {
        printf("Usage: ./substition KEY\n");
        return 1;
    }

    int len = strlen(argv[1]);
    string key = argv[1];

    if (len != 26)
    {
        printf ("Key must contain 26 characters.\n");
        return 1;
    }
    for (int i = 0; i < len; i++)
    {
        if (!isalpha(key[i]))
        {
            printf("Key must only contain alphabetical characters\n");
            return 1;
        }
    }
    for (int i = 0; i < len; i++)
    {
        for (int j = 0; j < len; j++)
        {
            if (i != j)
            {
                if (toupper(key[i]) == toupper(key[j]))
                {
                    printf("Key must not contain repeated characters\n");
                    return 1;
                }
            }
        }
    }

    // Promting user for text

    string text = get_string("plaintext: ");

    // Encipher
    for (int i = 0; i < strlen(key); i++)
    {
        key[i] = toupper(key[i]);
    }

    char ciphertext [strlen(text)+1];

    for (int i = 0; i < strlen(text); i++)
    {
        int n;


        if (isalpha(text[i]))
        {
            if (isupper(text[i]))
            {
                n = text[i] - 65;
                ciphertext [i] = toupper(key[n]);
            }
            else if (islower(text[i]))
            {
                n = text[i] - 97;
                ciphertext [i] = tolower(key[n]);
            }
        }
        else
        {
            ciphertext [i] = text[i];
        }
    }
    ciphertext[strlen(text)] = '\0';
    printf("ciphertext: %s",ciphertext);
    printf("\n");
}

