import numpy as np
def encode_hamming(parity_bits, data):
    n = len(data) + parity_bits
    assert 2 ** parity_bits == n + 1

    # copy data to code
    code = np.zeros(n, dtype=int)
    code[np.arange(n) & np.arange(n) + 1 > 0] = data
    # parity mask
    mask = np.zeros(n, dtype=int)
    num = 1
    while (num <= n):
        mask[num-1] = 1
        num *= 2
    # compute parity
    u = 0
    group = 2 ** u
    total_sum = 0
    index = -1
    for i in range (len(mask)):
        if mask[i] == 1:
            index = i
            while index < len(code):
                total_sum += code[index]
                for j in range(1, group):
                    index += 1
                    total_sum += code[index]
                index += (group + 1)
            if total_sum % 2 == 0:
                code[i] = 0
            else:
                code[i] = 1
            u += 1
            group = 2 ** u
            total_sum = 0

    # result
    return code

#Hamming Test
parity_bits = 3
data = np.random.randint(0, 2, 4) # generate 4 random data bits

# generate code
code = encode_hamming(parity_bits, data) # encode here
print('hamming code', data, '->', code)
