#include "shell.h"

/**
* _strlen - Calculates the legnth of a string
* @s: holds string array
*
* Return: Parameter length (the length of the string)
*/
int _strlen(char *s)
{
	int length = 0;

	while (*s != '\0')
	{
		length++;
		s++;
	}

	return (length);
}
