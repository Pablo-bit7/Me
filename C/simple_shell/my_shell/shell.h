#ifndef SHELL_H
#define SHELL_H

/* ================ Header files =============== */
#include <stdio.h>
#include <string.h>
#include <stdarg.h>
#include <stdlib.h>
#include <limits.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/* ============= Function prototypes ============ */
int _printf(const char *format, ...);
void _prompt(void);
ssize_t read_input(char *buffer, size_t size);
char **tokenize(char *str, char *delim);
void execute_command(char **command);

/* Print helper functions */
int _putchar(char c);
int _print_str(char *str);
int _print_int(int n);
int _print_uint(unsigned int n);
int _print_oct(unsigned int n);
int _print_ptr(void *ptr);
int _print_hex(unsigned int n, int uppercase);
int _print_rev_str(char *str);

/* Helper functions */
int is_delim(char c, char *delim);
int _strcmp(char *s1, char *s2);
void print_environment(void);
void execute_external_command(char **command, char **envp);

#endif /* SHELL_H */
