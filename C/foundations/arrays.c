#include <stdio.h>
#include <stdlib.h>

/* Everything to do with ARRAYS */

int main()
{
    int luckyNumbers[] = {4, 8, 15, 16, 23, 42}; //specify the data type of the elements to be stored in the array
    printf("%d", luckyNumbers[5]); // call specific elements in an array by using its index

    luckyNumbers[1] = 200; // modify elements in chosen index like so
    printf("%d", luckyNumbers[1]);

    int randomNumbers[50]; // make an empty array by telling the commputer how many elements to expect (50)

    char myName[30] = "Paballo Mogane"; // this in essence also an example of an array
    printf("%s", myName);


    return 0;
}