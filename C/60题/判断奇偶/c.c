#include<stdio.h>
#include<stdlib.h>
int main(void)
{
    long long shu ;
    puts("请输入数字");
    if(scanf("%lld", &shu)!=1)
    {
        puts("输入无效");
        exit(EXIT_FAILURE);
    }

    if(shu > 0)
    {
        if(shu%2==1)
        {
            puts("是奇数");
        }
        if(shu%2==0)
        {
            puts("是偶数");
        }
    }
    if(shu<0)
    {
        puts("输入无效");
        exit(EXIT_FAILURE);
    }

    return 0;
}