// Variables

#include <stdio.h>
#include <stdbool.h> // header for bool datatype/variable

int main(){
    int a = 5;
    float b = 3.14;
    char c = 'a';
    double d = 1.23456789;
    bool boo = true;

    printf("%i \n", a);
    printf("%.2f \n", b);
    printf("%c \n", c);
    printf("%lf \n", d);
    printf("%d \n", boo);

    // Variable from input

    int e;
    printf("Enter any integrer: ");
    scanf("%i", &e);
    printf("Your Input is %i\n", e);

    // Constant

    const float SPEEDOFLIGHT = 9.8;
    printf("%.2f", SPEEDOFLIGHT);

    return 0;
}
