#include<stdio.h>

int main(void)
{
    int year;

    printf("input year:");
    scanf("%d", &year);

    if((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0))
    {
        printf("%d is leap year\n", year);
        printf("Feb have 29 days\n");
    }
    else
    printf("%d is not leap year\n", year);
    return 0;
}