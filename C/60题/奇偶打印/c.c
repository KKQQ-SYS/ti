#include<stdio.h>
#include<stdlib.h>

int main(void)
{
    int shu;

    printf("请输入\n");
    if(scanf("%d", &shu)!=1)
    {
        printf("输入无效\n");
        exit(EXIT_FAILURE);
    }
    if(shu < 0)
    {
        printf("输入无效\n");
        exit(EXIT_FAILURE);
    }

    if(shu % 2 == 0)
        printf("偶数，是%d\n", shu);
    else
        printf("奇数，是%d\n", shu);
    return 0;
}