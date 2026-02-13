#include <stdio.h>
int main(void)
{
    double a;
    printf("\aaaaaaaaaaaaa");
    printf("$qqqqqqqqqqqqqqq_\b\b\b\b\b\b\b\b\b");
    scanf("%lf",&a);
    printf("\n\t$%.2f  a  month  is  $%.2f  a  year.",a,a*12.0);
    printf("\rGee!\n");
    
    return 0;
}