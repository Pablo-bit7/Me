#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* Working with numbers in C */

int main()
{
    printf("%f", 8 + 5.6); //'%f' format specifier allows us to pass and returns float data type

    // we can also do the four basic math opperations with & within various functions

    printf("%f", pow(5, 3)); // pow() allows us to raise first num to the power of the second

    printf("%f", sqrt(25)); // sqrt() gives us the square of a num

    printf("%f", ceil(36.356)); // ceil() rounds UP to nearest whole

    printf("%f", floor(36.656)); // floor() rounds DOWN to nearest whole


    return 0;
}