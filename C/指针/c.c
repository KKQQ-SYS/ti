#include <stdio.h>

int main() {
    char buf[10];

    printf("puts@addr = %p\n", (void*)puts);

    gets(buf);

  // 经典栈溢出漏洞点（危险）
    return 0;
}
