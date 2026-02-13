#include <stdio.h>
int factorial(int n) {
    //递归的出口
    if (n == 1 || n == 0) {
        return 1;
    }
    //函数调用自身
    return n * factorial(n - 1);
}
int main()
{
    int n;
    scanf("%d", &n);
    printf("%d! = %d", n,factorial(n));
    return 0;
}