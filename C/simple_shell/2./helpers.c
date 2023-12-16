#include "shell.h"

/**
 * is_delim - Func checks if a character is a delimiter
 * @c: The character to be checked
 * @delim: The array of delimiter characters
 * Return: 1 if it is a delimiter, 0 if it is not
 */
int is_delim(char c, char *delim)
{
	while (*delim)
		if (*delim++ == c)
			return (1);

	return (0);
}

/**
 * _strcmp - compares two strings
 * @s1: holds first string
 * @s2: holds second string
 *
 * Return: s1 - s2 (diff in ASCII values)
 */
int _strcmp(char *s1, char *s2)
{
	while (*s1 != '\0' && *s2 != '\0')
	{
		if (*s1 != *s2)
		{
			return (*s1 - *s2);
		}
		s1++;
		s2++;
	}

	return (*s1 - *s2);
}

/**
 * print_environment - Prints the current environment.
 */
void print_environment(void)
{
    extern char **environ;
    int i = 0;

    while (environ[i] != NULL)
    {
        _printf("%s\n", environ[i]);
        i++;
    }
}

/**
 * execute_external_command - Executes an external command.
 * @command: An array of strings representing the command and its arguments.
 *
 * Return: The exit status of the command.
 */
void execute_external_command(char **command, char **envp)
{
    pid_t child_pid;

    child_pid = fork();

    if (child_pid == -1)
    {
        perror("Error forking process");
        exit(EXIT_FAILURE);
    }

    if (child_pid == 0) // Child process
    {
        if (execve(command[0], command, envp) == -1)
        {
            perror("Error executing command");
            exit(EXIT_FAILURE);
        }
    }
    else // Parent process
    {
        // Wait for the child process to complete
        waitpid(child_pid, NULL, 0);
    }
}
