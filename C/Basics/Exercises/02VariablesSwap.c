#include <stdio.h>

int main(){
    int a = 10;
    int b = 20;

    printf("Values before swaping : %i & %i\n", a, b);

    a = a + b;
    b = a - b;
    a = a - b;

    printf("Values after swaping : %i & %i\n", a, b);

    return 0;
}