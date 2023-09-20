#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
* main - Fork + wait + execve example
*
* Return: Always 0.
*/
int main(void)
{
    int i;
    pid_t child_pid;
    int status;

    for (i = 0; i < 5; i++)
    {
        child_pid = fork();

        if (child_pid == -1)
        {
            perror("Error:");
            return (1);
        }

        if (child_pid == 0)
        {
            /* This code runs in the child process */
            char *args[] = {"/bin/ls", "-l", "/tmp", NULL};
            if (execve("/bin/ls", args, NULL) == -1)
            {
                perror("execve");
                return (1);
            }
        }
        else
        {
            /* This code runs in the parent process */
            wait(&status);
            printf("Child process with PID %d has exited\n", child_pid);
        }
    }

    return (0);
}
