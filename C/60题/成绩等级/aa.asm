.intel_syntax noprefix
.LC0:
        .string "\350\257\267\350\276\223\345\205\245\344\275\240\347\232\204\346\210\220\347\273\251"
.LC1:
        .string "%d"
.LC2:
        .string "\344\275\240\347\232\204\347\255\211\347\272\247\344\270\272\357\274\232"
.LC3:
        .string "\350\276\223\345\205\245\346\227\240\346\225\210"
.LC4:
        .string "A"
.LC5:
        .string "B"
.LC6:
        .string "C"
.LC7:
        .string "D"
.LC8:
        .string "E"
main:
        sub     rsp, 24
        mov     edi, OFFSET FLAT:.LC0
        call    puts
        xor     eax, eax
        lea     rsi, [rsp+12]
        mov     edi, OFFSET FLAT:.LC1
        call    __isoc99_scanf
        cmp     eax, 1
        jne     .L2
        cmp     DWORD PTR [rsp+12], 100
        ja      .L2
        mov     edi, OFFSET FLAT:.LC2
        xor     eax, eax
        call    printf
        mov     eax, DWORD PTR [rsp+12]
        cmp     eax, 89
        jg      .L12
        cmp     eax, 79
        jg      .L13
        cmp     eax, 69
        jg      .L14
        cmp     eax, 59
        jle     .L8
        mov     edi, OFFSET FLAT:.LC7
        call    puts
        jmp     .L5
.L13:
        mov     edi, OFFSET FLAT:.LC5
        call    puts
.L5:
        xor     eax, eax
        add     rsp, 24
        ret
.L12:
        mov     edi, OFFSET FLAT:.LC4
        call    puts
        jmp     .L5
.L8:
        mov     edi, OFFSET FLAT:.LC8
        call    puts
        jmp     .L5
.L14:
        mov     edi, OFFSET FLAT:.LC6
        call    puts
        jmp     .L5
        
.L2:
        mov     edi, OFFSET FLAT:.LC3
        call    puts
        mov     edi, 1
        call    exit
