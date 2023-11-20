#include <stdio.h>
#include <stdlib.h>

/**
* main - Entry point of the program
*
* Description: This program prints "$ ", waits for the user to enter a
*              command, and then prints the entered command on the next line.
*              It continues to prompt for input until the user signals the
*              end-of-file (EOF) by pressing Ctrl+D (Linux/Unix) or Ctrl+Z
*              (Windows).
*
* Return: Always 0
*/
int main(void)
{
    char *line = NULL;
    size_t len = 0;
    ssize_t read;

    printf("$ ");

    while ((read = getline(&line, &len, stdin)) != -1)
    {
        printf("%s$ ", line);
    }

    free(line);

    return (0);
}
