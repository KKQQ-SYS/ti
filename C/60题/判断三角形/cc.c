#include<stdio.h>

int main(void)
{
    float a,b,c;
    printf("input a b c\n");
    scanf("%f%f%f", &a, &b, &c);
    if(a + b > c && b + c > a && a + c > b)
        if(a == b && b == c)
            printf("This is a deng bian trangle\n");
        else
            printf("This is a qrdinary trianqle\n");
    else
        printf("This is not a triangle\n");

    return 0;
}