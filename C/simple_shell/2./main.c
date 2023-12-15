#include "shell.h"

int main(void)
{
    char *input_result;
    char **tokenized_command;
    size_t buffer_size = 120;

    while (1)
    {
        _prompt();
        input_result = read_input(&buffer_size);

        if (_strcmp(input_result, "exit") == 0 || input_result == EOF)
        {
            _printf("\n");
            free(input_result);  // Free the allocated memory
            break;
        }

        if (input_result[0] == '\0')  // Empty string means end of input
            _printf("\n");

        if (input_result[0] != '\0')
        {
            tokenized_command = tokenize(input_result, " ");

            /* Execute the command (You need to implement this function) */
            execute_command(tokenized_command);

            // Free the allocated memory for the tokenized command
            // You need to implement a function to free the memory of tokenized_command
            // free_tokenized_command(tokenized_command);

            free(input_result);  // Free the allocated memory
        }
    }

    return (0);
}
