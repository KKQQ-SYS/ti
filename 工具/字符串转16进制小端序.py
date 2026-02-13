# 将字符串转换为16进制，并按字节顺序拼接，确保每组有4字节
def str_to_hex(input_string):
    if not input_string:  # 检查是否是空字符串
        return "输入字符串为空，请提供有效的字符串。"

    # 将字符串转换为16进制
    hex_values = ''.join([hex(ord(c))[2:].zfill(2) for c in input_string])
    
    # 将16进制按字节顺序反转
    reversed_hex = ''.join([hex_values[i:i+2] for i in range(0, len(hex_values), 2)][::-1])

    # 确保每组为4字节（8个字符），不足的部分补零
    reversed_hex = reversed_hex.ljust((len(reversed_hex) + 7) // 8 * 8, '0')

    # 按每4字节（8个字符）分割
    hex_parts = [f"0x{reversed_hex[i:i+8]}" for i in range(0, len(reversed_hex), 8)]

    return ' '.join(hex_parts)

# 测试
input_string = input("请输入要转换的字符串：")
hex_output = str_to_hex(input_string)
print("按小段序排列的16进制表示为:", hex_output)
