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
void _print(const char *format);
void _prompt(void);

/* Print helper functions */
int _strlen(char *s);

#endif /* SHELL_H */
