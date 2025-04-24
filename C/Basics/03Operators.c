// Operators

#include <stdio.h>

int main(){
    // Arithmetic Operator

    printf("%d\n",20 + 10); // Addition
    printf("%d\n",20 - 10); // Subtraction
    printf("%d\n",20 * 10); // Multiplication
    printf("%d\n",20 / 10); // Division
    printf("%d\n",20 % 10); // Modulus

    int x = 10;

    printf("%d\n", ++x); // Increment
    printf("%d\n", --x); // Decrement
    
    // Assignment Operator

    int a = 1;
    a += 1;
    a -= 1; 
    a *= 1;
    a /= 1;
    a %= 1;
    
    // Comparision Operator

    printf("%d\n", 10 == 10); // Equal
    printf("%d\n", 10 != 10); // Not Equal
    printf("%d\n", 100 > 10); // Greater than
    printf("%d\n", 10 < 100); // Less than
    printf("%d\n", 10 >= 10); // Greater than equal to
    printf("%d\n", 10 <= 10); // Less than equal to

    // Logical Operator

    printf("%i\n", 100 > 10 && 10 > 1); // AND
    printf("%i\n", 100 > 10 || 100 < 10); // OR
    printf("%i\n", !(5 > 4)); // NOT

    return 0;
}