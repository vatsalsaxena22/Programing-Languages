// Datatypes

#include <stdio.h>
#include <stdbool.h> // for boolean

int main(){
    int a = 5; // integar - 2 or 4 bytes
    float b = 3.14; // float - 4 bytes
    char c = 'a'; // char - 1 byte
    double d = 3.14159; // double - 8 bytes
    bool e = false; // bool - 1 byte

    printf("%d \n", a);
    printf("%.4f \n", b);
    printf("%c \n", c);
    printf("%lf \n", d);
    printf("%d \n", e);

    printf("%lu \n", sizeof(a));
    printf("%lu \n", sizeof(b));
    printf("%lu \n", sizeof(c));
    printf("%lu \n", sizeof(d));
    printf("%lu \n", sizeof(e));

    // Type Conversion

    int num1 = 5;
    int num2 = 2;
    float sum = (float) num1 / num2;
    printf("%.2f", sum);

    return 0;
}