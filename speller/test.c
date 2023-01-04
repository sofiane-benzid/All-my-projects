// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include "dictionary.h"
#include <stdio.h>
#include <strings.h>
#include <string.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];
int words = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int word_hash = hash(word);
    for (node *tmp = table[word_hash]; tmp != NULL; tmp=tmp->next)
    {
        if (strcasecmp(tmp->word, word) == 0)
            return true;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE* dict = fopen(dictionary, "r");

    if (dict == NULL)
        return false;

    char w[LENGTH + 1];

    while (fscanf(dict, "%s", w) != EOF)
    {
        node * n = malloc(sizeof(node));
        if (n == NULL)
            return false;

        strcpy(n->word, w);
        n->next = table[hash(w)];
        table[hash(w)] = n;
        words++;
    }
    fclose(dict);

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    if (words > 0)
        return words;
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        for (node *tmp = table[i]; cursor != NULL; tmp=tmp->next, cursor = cursor->next)
        {
            free(tmp);
        }
    }
    return true;
}
