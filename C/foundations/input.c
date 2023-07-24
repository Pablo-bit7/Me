#include <stdio.h>
#include <stdlib.h>

/* Everything about taking input from the user */

int main()
{
    int age;
    printf("Please enter your age: "); // first prompt the user like so
    scanf("%d", &age); // use 'scanf()' function to take input and assign it to a variable using '&'
    /* '&<variable>' is known as a POINTER */
    printf("You are %d years old.", age);


    double gpa;
    printf("Please enter your gpa: ");
    scanf("%lf", &gpa); // '%lf' format specifier tells 'scanf()' function to recieve double data type
    printf("Your GPA is %f.", gpa);


    char grade;
    printf("What is your grade?: ");
    scanf("%c", &grade); // use '%c'format specifier to take 1 CHARACTER and '&' pointer to assign it
    printf("Your grade is %c.", grade);


    char name[20]; // we need to tell the computer to allocate memory for a STRING (20 characters)
    printf("What's your name?: ");
    scanf("%s", name); // we DON'T need '&' to assign input of char data type IF STRING
    printf("Your name is %s. Welcome!", name);


    char full_names[40];
    printf("Please write you full names: ");
    fgets(full_names, 40, stdin);
    printf("Your name is %s. Welcome!", full_names);
    /*
    The 'fgets(x, y, z)' function assigns via the 'x', allocates memory with the 'y'
    and tells the computer where from to take the input with the 'z' fields
    respectively. In this case we've told the computer to take input from the standard
    input ("stdin") in the 'z' field.

    We use this function when expecting a STRING WITH SPACES IN IT like "Paballo Mogane"
        */


    return 0;
}