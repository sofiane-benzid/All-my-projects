#include <cs50.h>
#include <stdio.h>
#include <string.h>

#define MAX 9

typedef struct
{
    string name;
    int votes;
}
candidate;

candidate candidates[MAX];

int candidate_count;

void print_winner(void);
bool vote(string name);

int main(int argc, string argv[])
{
    if (argc < 2)
    {
        printf("Usage: ./plurality [candidate...]\n");
        return 1;
    }

    candidate_count = argc - 1;

    if (candidate_count > MAX)
    {
        printf ("Maximum number of candidates is %i\n", MAX);
        return 1;
    }

    for (int i = 0 ; i < candidate_count; i++)
    {
        candidates[i].name = argv[i+1];
        candidates[i].votes = 0;
    }

    for (int i = 0 ; i < candidate_count; i++)
    {
        string name = get_string ("Vote: \n");
        if (!vote(name))
        {
            printf("Invalid vote\n");
        }
    }
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    // TODO
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(name, candidates[i].name) == 0)
        {
            candidates[i].votes++;
            return true;
        }
    }
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    int winner = 0;
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes > winner)
            winner = candidates[i].votes;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes == winner)
            printf("%s\n", candidates[i].name);
    }
    return;
}