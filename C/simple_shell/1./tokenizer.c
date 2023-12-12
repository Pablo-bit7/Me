#include "shall.h"

int main ()
{
    char command[] = "my name is Pablo";

    char *token, *delim;
    delim = " ";

    token = strtok(command, delim);

    while (token != NULL)
    {
        printf("Token %s\n", token);
        token = strtok(NULL, delim);
    }

    return (0);
}
