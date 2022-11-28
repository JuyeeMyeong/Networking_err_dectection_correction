import numpy as np
def encode_crc(data):
    crc = format(263, 'b') # CRC-8 263
    crcList = [int(x) for x in list(crc)]
    n = len(data) + len(crcList) - 1
    
    # copy data to code
    resultCode = np.zeros(n, dtype=int)
    code = np.zeros(n, dtype=int)
    code[:len(data)] = data
    resultCode[:len(data)] = data

    for i in range (n - (len(crcList) - 1)):
        if code[i] == 1:
            part = code[i : i + len(crcList)]
            for j in range(len(crcList)):
                code[i + j] = xor(part[j], crcList[j])

    resultCode[n - (len(crcList) - 1) :] = code[len(data):]
    return resultCode
  
  def decode_crc(data):
    crc = format(263, 'b') # CRC-8
    crcList = [int(x) for x in list(crc)]
    n = len(data)
    # copy data to code
    code = np.zeros(n, dtype=int)
    code = data

    remainder = 0
    for i in range (n - (len(crcList) - 1)):
        if code[i] == 1:
            part = code[i : i + len(crcList)]
            for j in range(len(crcList)):
                code[i + j] = xor(part[j], crcList[j])
    errorSum = code[len(data) - len(crcList) + 1: ]

    return errorSum
  
  
data = [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0]
print(data)
data = encode_crc(data)
print(data)
print(decode_crc(data))

#CRC test
data = np.random.randint(0, 2, 16)
print('Data to transmit =',data)
data = encode_crc(data)
print('After data =', data)
data[np.random.randint(0,len(data))] ^= 1
data[np.random.randint(0,len(data))] ^= 1
data[np.random.randint(0,len(data))] ^= 1
#data[22] ^= 1
print('Error data =', data)
result = decode_crc(data)
if sum(result) != 0:
    print('An error detected. Remainder =', result)
else:
    print('No error detected. Remainder =', result)
