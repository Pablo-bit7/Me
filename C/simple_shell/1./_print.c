#include "shell.h"

/**
 * _print - Writes a string to standard output.
 * @format: The string to be printed.
 */
void _print(const char *format)
{
    if (format != NULL)
        write(1, format, _strlen(format));
}
