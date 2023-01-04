#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score (string word);

int main (void)
{
    string word1 = get_string ("Player 1: ");
    string word2 = get_string ("Player 2: ");

    int score1 = compute_score (word1);
    int score2 = compute_score (word2);

    if (score1 > score2)
        printf ("Player 1 wins!");
    else if (score1 == score2)
        printf ("Tie\n");
    else
        printf ("Player 2 wins!");

}

int compute_score(string word)
{
    int counter = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        if (isupper(word[i]))
            counter += POINTS[word[i] - 65];
        if (islower(word[i]))
            counter += POINTS[word[i] - 97];
    }
    return counter;
}