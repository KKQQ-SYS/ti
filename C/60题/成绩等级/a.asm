section .data
    msg db "Hello, Assembly!", 0xA  ; 0xA 是换行符 (\n)
    len equ $ - msg                 ; 计算字符串长度

section .text
    global _start

_start:
    ; --- 调用系统服务打印字符串 (sys_write) ---
    mov rax, 1          ; 系统调用号 1 是 write
    mov rdi, 1          ; 文件描述符 1 是 stdout (标准输出)
    mov rsi, msg        ; 字符串的内存地址
    mov rdx, len        ; 字符串的长度
    syscall              ; 触发软中断，交给内核执行

    ; --- 调用系统服务退出程序 (sys_exit) ---
    mov rax, 60         ; 系统调用号 60 是 exit
    xor rdi, rdi        ; 退出状态码 0 (xor 自己等于清零)
    syscall  

       