#include <stdio.h>
#include <unistd.h>

/**
* main - PPID
*
* Return: Always 0
*
* Description: This program retrieves & prints the process ID
* of the parent process of this program on execution
*/
int main(void)
{
	pid_t parent_pid;

	parent_pid = getppid();
	printf("Parent Process PID: %u\n", parent_pid);

	return (0);
}
