from kk import*
context(arch='i386', os='linux')
#context(arch='amd64', os='linux')
#p = remote('192.168.127.12', 10001)
p = process('./pwn')
elf = ELF('./pwn')
libc = ELF('/lib/i386-linux-gnu/libc.so.6')
#libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

