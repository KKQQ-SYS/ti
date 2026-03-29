section .data
    msg db 'Hello, world!', 0xA  ; 0xA 是换行符的 ASCII 码

section .text
    global _start

_start:
    ; 调用 write 系统调用 (sys_write)
    mov rax, 1          ; 系统调用号 1 是 write
    mov rdi, 1          ; 文件描述符 1 是标准输出 (stdout)
    mov rsi, msg        ; 字符串的地址
    mov rdx, 14         ; 字符串的长度
    syscall             ; 执行系统调用

    ; 调用 exit 系统调用 (sys_exit)
    mov rax, 60         ; 系统调用号 60 是 exit
    xor rdi, rdi        ; 退出码为 0
    syscall

