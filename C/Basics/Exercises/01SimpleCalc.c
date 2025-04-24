#include <stdio.h>

int main(){
    printf("Welcome to Simple C Calculator!\n");

    int num1, num2;

    printf("Please Enter your first Number: ");
    scanf("%i", &num1);
    
    printf("Please Enter your second Number: ");
    scanf("%i", &num2);

    printf("The Addition of %i and %i is %i.\n", num1, num2, (num1 + num2));
    printf("The Subtraction of %i and %i is %i.\n", num1, num2, (num1 - num2));
    printf("The Multiplication of %i and %i is %i.\n", num1, num2, (num1 * num2));
    printf("The Division of %i and %i is %i.\n", num1, num2, (num1 / num2));

    return 0;
}