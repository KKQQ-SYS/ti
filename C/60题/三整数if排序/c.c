#include<stdio.h>
#include<stdlib.h>

int main(void)
{
    int shu[3];
    int i = 0;
    int N = 3;

    for(i=0;i<N;i++)
    {
        printf("请输入第%d数字:",i +1);
        if(scanf("%d",&shu[i])!=1)
        {
            puts("输入无效");
            exit(EXIT_FAILURE);
        }
        if(shu[i]<0)
        {
            puts("输入无效");
            exit(EXIT_FAILURE);
        }
    }

    for(int i=0; i<N-1; i++)
    {
        for(int j =0; j<N-1-i; j++)
        {
            if(shu[j] < shu[j + 1])
            {
                int temp = shu[j];
                shu[j] = shu[j + 1];
                shu[j + 1] = temp;
            }
        }
    }
    printf("从大到小排序:");
    for(i =0; i < N; i++)
    {
        printf("%d  ",shu[i]);
    }
    printf("\n");

    return 0;
}