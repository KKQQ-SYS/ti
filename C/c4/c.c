#include<stdio.h>
int main(void)
{
    float a = 32000.0;
    double b = 2.14e9;
    long double c = 5.32e-5;
    printf("a = %e\n", a);
    printf("b = %le\n", b);
    printf("c = %.20Lf\n", c);
    return 0;
}
