def xor(a, b):
    result = []
    for i in range(1, len(b)):
        result.append('1' if a[i] != b[i] else '0')
    return ''.join(result)

def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(tmp, divisor) + dividend[pick]
        else:
            tmp = xor('0'*pick, tmp) + dividend[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(tmp, divisor)
    else:
        tmp = xor('0'*pick, tmp)

    return tmp

def encode_data(data, divisor):
    l_key = len(divisor)
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, divisor)
    codeword = data + remainder
    return codeword

# Input
data = "1101011011"  # Data to be transmitted
divisor = "10011"    # Generator polynomial

print("Input Data: ", data)
print("Divisor: ", divisor)

codeword = encode_data(data, divisor)
print("Encoded Data (Codeword): ", codeword)
