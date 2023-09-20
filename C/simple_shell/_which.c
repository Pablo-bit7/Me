#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

/**
* findFileInPath - Search for a file in the PATH and print its full path if found.
* @filename: The name of the file to search for.
* @path: The PATH environment variable.
*/
void findFileInPath(const char *filename, const char *path)
{
    char *token;
    char *pathCopy = strdup(path);

    if (pathCopy == NULL)
    {
        perror("Memory allocation error");
        exit(EXIT_FAILURE);
    }

    /* Tokenize the PATH using ':' as the delimiter */
    token = strtok(pathCopy, ":");
    while (token != NULL)
    {
        /* Create the full path by combining the directory and filename */
        char fullPath[1024];  /* Assuming maximum path length */
        snprintf(fullPath, sizeof(fullPath), "%s/%s", token, filename);

        /* Check if the file exists at the full path */
        if (access(fullPath, F_OK) == 0)
        {
            printf("%s\n", fullPath);
            free(pathCopy);
            return;
        }

        /* Move to the next token in the PATH */
        token = strtok(NULL, ":");
    }

    free(pathCopy);
}

/**
* main - Entry point of the program.
* @argc: The number of command-line arguments.
* @argv: An array of strings containing the command-line arguments.
* Return: Always 0.
*/
int main(int argc, char *argv[])
{
    int i;

    if (argc < 2)
    {
        fprintf(stderr, "Usage: %s filename ...\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    /* Get the PATH environment variable */
    const char *path = getenv("PATH");
    if (path == NULL)
    {
        fprintf(stderr, "PATH environment variable not found\n");
        exit(EXIT_FAILURE);
    }

    /* For each filename provided as an argument, search for it in the PATH */
    for (i = 1; i < argc; i++)
    {
        findFileInPath(argv[i], path);
    }

    return (0);
}
