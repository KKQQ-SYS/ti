#include<stdio.h>

int main(void)
{
    int i;
    float shu[3];
    for( i = 0; i < 3;i++)
    {
        printf("输入，第%d条边\n", i + 1);
        scanf("%f", &shu[i]);
    }

    if((shu[0] + shu[1] <= shu[2]) || (shu[0] + shu[2] <= shu[1]) || (shu[1] + shu[2] <= shu[0]))
        printf("这不是一个是一个三角形\n");
    else
        {
            printf("这是一个三角形\n");
            if(shu[0] == shu[1] && shu[1] == shu[2])
                printf("这还是一个全等三角形\n");
        }
    return 0;

}