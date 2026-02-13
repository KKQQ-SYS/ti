#include <stdio.h>

int main() {
    unsigned int a = 3000000000;
    short b = 200;
    long c = 65537;
    long double d = 6.3L;
    long long r = -16;
    char s = '\n';
    //scanf("%d", &r);
    printf("a = %u and not %d\n",a,a);
    printf("b = %hd and %d\n",b,b);
    printf("c = %ld and not %hd\n",c,c);
    printf("d = %.40lf and not %llf\n",d,d);
    //printf("int size = %d\n",(int)sizeof(int));
    printf("s = %c\n",s);
    printf("int size = %d\n",(int)sizeof(float));
    printf("int size = %d\n",(int)sizeof(double));
    printf("int size = %d\n",(int)sizeof(long long));//sizeof
    printf("r = %lx\n",r);
    printf("s = %c\n",s);
    return 0 ;
}

int m