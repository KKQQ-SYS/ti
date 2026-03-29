#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mman.h>
#include <signal.h> // ensure 32-bit compatibility
 
int main()
{
    // 关闭缓冲区
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
 
    // 分配可执行内存
    size_t size = 4096;
    void *buf = mmap(NULL, size,
                     PROT_READ | PROT_WRITE | PROT_EXEC,
                     MAP_ANONYMOUS | MAP_PRIVATE,
                     -1, 0);
    if (buf == MAP_FAILED)
    {
        perror("mmap");
        exit(1);
    }
 
    // 提示并读取 shellcode
    printf("Input shellcode (max %zu bytes):\n", size);
    ssize_t len = read(STDIN_FILENO, buf, size);
    if (len <= 0)
    {
        perror("read");
        exit(1);
    }
 
    printf("Received %zd bytes, executing...\n", len);
 
    // 执行 shellcode
    ((void (*)())buf)();
 
    return 0;
}
 
/*
32 位编译示例：
    gcc -m32 -fno-stack-protector -z execstack -no-pie exec_shellcode.c -o exec_shellcode32
运行：
    ./exec_shellcode32
然后将你的 32 位 shellcode 通过管道或输入导入程序。
*/