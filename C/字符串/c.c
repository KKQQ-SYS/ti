#include <stdio.h>
#include <string.h>
#define A 62.4
int main(void)
{
    float weigh,volume;
    int size,letters;
    
    char name[0];
    printf("Hi! What's your name?\n");
    scanf("%s",name);
    printf("%s, what's your weight in pounds?\n",name);
    scanf("%f",&weigh);

    size = sizeof(name);
    volume = weigh / A;
    printf("Your weight in pounds is %s, and your volume in cubic feet is %22.2f.\n",name,volume);
    printf("Also, your first name has %d letters.\n",letters);
    printf("and we have %d letters in total.\n", size);
    return 0;
}