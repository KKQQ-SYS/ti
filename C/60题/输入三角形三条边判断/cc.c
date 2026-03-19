#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

int main(void)
{
    double s[3];
    int i;

    for(i = 0; i < 3; i++)
    {
        printf("请输入第%d条边: ", i + 1);
        if(scanf("%lf", &s[i]) != 1 || s[i] <= 0) 
        {
            printf("输入无效\n");
            return EXIT_FAILURE;
        }       
    }

    if(!(s[0] + s[1] > s[2] && s[0] + s[2] > s[1] && s[1] + s[2] > s[0]))
    {
        printf("这三条边无法组成三角形\n");
        return 0;
    }

    printf("这是一个：");

    bool isEquilateral = (s[0] == s[1] && s[1] == s[2]);
    bool isIsosceles = (s[0] == s[1] || s[0] == s[2] || s[1] == s[2]);

    bool isRight = (s[0]*s[0] + s[1]*s[1] == s[2]*s[2] ||
                    s[0]*s[0] + s[2]*s[2] == s[1]*s[1] ||
                    s[1]*s[1] + s[2]*s[2] == s[0]*s[0]);

    if(isEquilateral)
        printf("等边三角形");
    else if(isIsosceles)
        printf("等腰三角形");
    else
        printf("普通三角形");

    if(isRight)
    {
        printf("，且是直角三角形");
    }

    printf("\n");

    return 0;
}