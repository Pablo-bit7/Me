#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* MY_CALCULATOR 1.0 */

int main()
{

    int num_1; // variable declaration
    int num_2;

    printf("\nHi! I'm your addition buddy.\nEnter two numbers and get their sum.\n"); // initial prompt

    printf("\nEnter the 1st number: "); // prompt user for first input
    scanf("%d", &num_1); // input assignment must come right after input prompt
    printf("\nEnter the 2nd number: ");
    scanf("%d", &num_2);

    int sum = num_1 + num_2; // logic for sum is stored in a variable to be called later

    printf("\nThe sum of %d and %d is equal to %d", num_1, num_2, sum);

    printf("\nBye!\n");


    return 0;
}