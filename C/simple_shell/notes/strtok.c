#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * splitString - Split a string into words based on a delimiter.
 * @input: The input string to be split.
 * @delimiter: The delimiter used to split the input.
 * @wordCount: A pointer to an integer to store the word count.
 *
 * Return: An array of strings containing the split words.
 */
char **splitString(const char *input, const char *delimiter, int *wordCount)
{
    char **words = NULL;
    char *token;
    char *copy = strdup(input);
    int count = 0;

    if (copy == NULL)
    {
        perror("Error in memory allocation");
        exit(EXIT_FAILURE);
    }

    token = strtok(copy, delimiter);
    while (token != NULL)
    {
        count++;
        words = realloc(words, sizeof(char *) * count);

        if (words == NULL)
        {
            perror("Error in memory allocation");
            free(copy); /* Free duplicated input string */
            exit(EXIT_FAILURE);
        }

        words[count - 1] = strdup(token);
        token = strtok(NULL, delimiter);
    }

    free(copy);

    *wordCount = count;
    return words;
}

/**
 * main - Entry point of the program
 *
 * Description: This program splits a sample string into words and prints them.
 * It adheres to the Betty coding style and avoids memory leaks.
 *
 * Return: Always 0
 */
int main(void)
{
    const char *input = "This is a sample string";
    const char *delimiter = " ";
    int wordCount, i;

    char **words = splitString(input, delimiter, &wordCount);

    /* Print the split words */
    for (i = 0; i < wordCount; i++)
    {
        printf("Word %d: %s\n", i + 1, words[i]);
        free(words[i]); /* Free each word */
    }

    /* Free the array of words */
    free(words);

    return (0);
}
