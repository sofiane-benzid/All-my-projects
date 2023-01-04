#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    string key = argv[1];

    // Key validation: wrong key usage.
    if (argc != 2)
    {
        printf("Usage: ./substitution KEY\n");
        return 1;
    }
    // Key validation: wrong key length.
    else if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    // Key validation: only alphabetical characters and no repeated characters.
    for (int i = 0; i < 26; i++)
    {
        // Only alphabetical characters.
        if (!isalpha(key[i]))
        {
            printf("Key must only contain alphabetical characters.\n");
            return 1;
        }
        // No repeated characters
        for (int j = i + 1; j < 26; j++)
        {
            if (toupper(key[i])==toupper(key[j]))
            {
                printf("Key must not contain repeated characters.\n");
                return 1;
            }
        }
    }
    // Get plaintext
    string plaintext = get_string ("plaintext: ");
    // Encipher
    int difference [strlen(plaintext)];
    char output[strlen(plaintext)];
    for (int i = 0; i < strlen(plaintext) ; i++)
    {
        {
            if (isalpha(plaintext[i]))
            {
                if (isupper(plaintext[i]))
                {
                    difference[i] = plaintext[i] - 'A';
                    output[i] = key[difference[i]];
                }
                if (islower(plaintext[i]))
                {
                    difference[i] = plaintext[i] - 'a';
                    output[i] = key[difference[i]];
                }
            }
            else
            {
                output[i] = plaintext[i];
            }
        }
    }
    // Print ciphertext
    char ciphertext [strlen(plaintext)];
    for (int i = 0; i < strlen(plaintext); i++)
    {
        if (isupper(plaintext[i]))
        {
            ciphertext[i] = toupper(output[i]);
        }
        else if (islower(plaintext[i]))
        {
            ciphertext[i] = tolower(output[i]);
        }
        else
        {
            ciphertext[i] = output[i];
        }
    printf("%c", ciphertext[i]);
    }
    printf("\n");
    return 0;
}

