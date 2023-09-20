#include <stdio.h>
#include <unistd.h>

/**
* main - PID
*
* Return: Always 0.
*
* Description: This program retrieves & prints the process ID
* of this program on execution5
*/
int main(void)
{
	pid_t my_pid;

	my_pid = getpid();
	printf("Process PID: %u\n", my_pid);

	return (0);
}
