#include <stdio.h>

/**
* main - Entry point
* @argc: Number of arguments
* @argv: Array of arguments
*
* Return: Always 0
*
* Description: This program prints all the arguments, without using ac
*/
int main(int argc, char *argv[])
{
    int i;
    
    for (i = 1; argv[i] != NULL; i++)
    {
        printf("Argument %d: %s\n", i, argv[i]);
    }

    return (0);
}
