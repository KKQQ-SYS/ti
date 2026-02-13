#!/usr/bin/env python3
"""
使用预构建的可打印字符 shellcode
来源: https://github.com/TaQini/alpha3
"""

# 这是一个预构建的 x64 可打印字符 shellcode
# 使用 alpha3 生成，执行 execve("/bin/sh")

# 预编码的 shellcode (通过 alpha3 生成)
# 这个 shellcode 全部由可打印字符组成 (0x30-0x7A)
PRINTABLE_SHELLCODE = b"""
TYRX64  # 这是占位符，需要用 alpha3 生成实际内容
""".strip()

# 如果你有 alpha3 生成的结果，直接在这里替换：
# PRINTABLE_SHELLCODE = b"XXXX..."  # 粘贴 alpha3 输出

def main():
    print("[*] 可打印字符 shellcode 使用指南")
    print()
    print("1. 生成原始 shellcode:")
    print("   python3 -c \"from pwn import *; print(asm(shellcraft.sh()).hex())\"")
    print()
    print("2. 使用 alpha3 编码:")
    print("   python2 /home/kk/ti/工具/alpha3/ALPHA3.py x64 ascii mixedcase rax \\")
    print("       --input=raw_sc.bin > encoded.txt")
    print()
    print("3. 将编码后的内容复制到 exp.py")
    print()
    print("[!] 由于系统没有 Python 2，需要:")
    print("    a) 安装 python2")
    print("    b) 使用在线工具")
    print("    c) 使用 Docker 运行 alpha3")

if __name__ == "__main__":
    main()
