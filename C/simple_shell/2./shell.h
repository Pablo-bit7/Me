#ifndef SHELL_H
#define SHELL_H

/* ================ Header files =============== */
#include <stdio.h>
#include <string.h>
#include <stdarg.h>
#include <stdlib.h>
#include <limits.h>
#include <unistd.h>


/* ============ Function prototypes ============ */
int _printf(const char *format, ...);

/* Print helper functions */
int _putchar(char c);
int _print_str(char *str);
int _print_int(int n);
int _print_uint(unsigned int n);
int _print_oct(unsigned int n);
int _print_ptr(void *ptr);
int _print_hex(unsigned int n, int uppercase);
int _print_rev_str(char *str);

#endif /* SHELL_H */
