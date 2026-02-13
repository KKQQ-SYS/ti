#include <stdio.h>
#include<string.h>
#define A "Hello, World!"

int main(void)
{
    char name[40];
    const int a = 10;
    printf("What's your name?\n");
    scanf("%s",name);
    printf("Hello, %s.%s\n",name,A);
    printf("Your name has %ld letters.\n",strlen(name));
    printf("The first letter of your name is %d.\n",a);
    return 0;
}