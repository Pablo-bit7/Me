#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

#define MAX_INPUT_SIZE 1024

/**
* main - Simple shell program to execute commands with their full path.
*
* Return: Always 0.
*/
int main(void)
{
    char input[MAX_INPUT_SIZE];

    while (1)
    {
        /* Print the shell prompt */
        printf("#cisfun$ ");

        /* Read user input */
        if (fgets(input, sizeof(input), stdin) == NULL)
        {
            /* Handle EOF (Ctrl+D) to exit the shell */
            printf("\nGoodbye!\n");
            break;
        }

        /* Remove the newline character from the input */
        input[strcspn(input, "\n")] = '\0';

        /* Fork a new process to execute the command */
        pid_t child_pid = fork();

        if (child_pid == -1)
        {
            perror("fork");
            exit(1);
        }

        if (child_pid == 0)
        {
            /* This code runs in the child process */
            char *args[] = {input, NULL};

            /* Execute the command with its full path */
            if (execvp(input, args) == -1)
            {
                perror("execvp");
                exit(1);
            }
        }
        else
        {
            /* This code runs in the parent process */
            int status;
            waitpid(child_pid, &status, 0);

            if (WIFEXITED(status))
            {
                /* The child process has exited */
                printf("\nChild process exited with status %d\n", WEXITSTATUS(status));
            }
        }
    }

    return (0);
}
