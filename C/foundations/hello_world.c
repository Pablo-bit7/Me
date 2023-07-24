#include <stdio.h> /* This library stands for "standard input/output."
It contains functions for reading and writing data to and from the console or other input/output devices.
It provides functions like printf(), scanf(), fprintf(), and fscanf(). */

#include <stdlib.h> /* The "standard library" provides various general-purpose functions,
such as memory allocation, conversion, random number generation, sorting, and searching algorithms.
It includes functions like malloc(), free(), atoi(), rand(), qsort(), and bsearch(). */

int main()
{
    char name[] = "Paballo";
    int age = 22;

    printf("There was once a man named %s.\n", name); //'%s' used to call char data type

    //multiple variable calls must be written in the order in which they're calles

    printf("%s was %d years old.\n", name, age); //%d used to call int data type
    printf("He really liked his name...\n");
    printf("However, he did not like being %d years old.\n", age);


    return 0;
}