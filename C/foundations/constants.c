#include <stdio.h>
#include <stdlib.h>

/* CONSTANTS are variables that CAN'T BE MODIFIED */

int main()
{
    const int NUM = 8; // declare a constant variable with 'const'

    // use all caps to destinguish 'const' variables from others

    printf("%d", 90); // using numbers in this way also declares them as constants in C

    printf("Hello."); // strings are also considered constants


    return 0;
}