import numpy as np
def decode_hamming(code):
    n = len(code)

    # parity mask
    mask = np.zeros(n, dtype=int)
    num = 1
    while (num <= n):
        mask[num-1] = 1
        num *= 2
    # compute parity

    index = -1
    j = -1
    total_sum = 0
    u = 0
    group = 2 ** u
    errors = []
    for i in range (len(mask)):
        if mask[i] == 1:
            index = i
            while index < len(code):
                total_sum += code[index]
                for j in range (1, group):
                    index += 1
                    total_sum += code[index]
                index += (group + 1)
            if total_sum % 2 != 0:
                errors.insert(len(errors) - u, 1)
            else:
                errors.insert(len(errors) - u, 0)
            u += 1
            j -= 1
            group = 2 ** u
            total_sum = 0
            
    binary = 0
    for x in range(len(errors)):
        u -= 1
        if errors[x] == 1:
            binary += 2 ** u
    error = binary - 1
        
    if not errors:
        return -1, data
        
    # fix error
    if error >= 0:
        code[error] ^= 1

    # get data from code
    data = code[np.arange(n) & np.arange(n) + 1 > 0]

    # result
    return error, data
