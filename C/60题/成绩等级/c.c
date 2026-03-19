#include<stdio.h>
#include<stdlib.h>

int main(void)
{
    int shu;

    printf("请输入你的成绩\n");
    if(scanf("%d", &shu) != 1 || shu < 0 || shu > 100)
    {    
        printf("输入无效\n");
        exit(EXIT_FAILURE);
    }
    
    printf("你的等级为：");
    if(shu >= 90)
        printf("A\n");
    else if(shu >= 80)
        printf("B\n");
    else if(shu >= 70)
        printf("C\n");
    else if(shu >= 60)
        printf("D\n");
    else
        printf("E\n");

    return 0;
}