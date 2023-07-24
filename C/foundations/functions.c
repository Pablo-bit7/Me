#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* Everything about FUNCTIONS */

int main()
{
    sayHi();
    
    return 0;
}

// the 'int main()' is known as the main function/method but you can define functions as well
// you have to tell the comp the return type of a function (e.g 'int' in 'int main()')



void sayHi() // 'void' tells the comp that this function doesn't returning anything
{
    printf("Hello user!");
}

// to execute the code in the 'sayHi' function you'd need to CALL THE FUNCTION