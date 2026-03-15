#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    double *plt;
    int max;
    int number;
    int i = 0;

    puts("What  is the maximum number of type double entries?");
    if(scanf("%d",&max)!=1)
    {
        puts("输入无效");
        exit(EXIT_FAILURE);
    }

    plt = (double*)malloc(max * sizeof(double));

    if(plt == NULL)
    {
        puts("分配失败");
        exit(EXIT_FAILURE);
    }
    
    puts("已有指向max的数组有:");

    while (i  < max && scanf("%lf",&plt[i]) == 1)     
    {
        ++i;
        /* code */
    }

    printf("有%d", number = i);//5

    for(i = 0; i < number; i++)
    {
        printf("%7.2f  ",plt[i]);
    }
    puts("\n");
    
    free(plt);
    return 0;
}