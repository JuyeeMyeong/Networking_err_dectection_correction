def encode_2d(data):
    code = []

    for d in data:
        counts = d.count(1)
        if counts % 2 == 0:
            d.append(0)
        else:
            d.append(1)
            
    data_last = []
    last = []
    for j in range(len(data[0])):
        for l in range(len(data)):
            last.append(data[l][j])
        counts = last.count(1)
        if counts % 2 == 0:
            data_last.append(0)
        else:
            data_last.append(1)
        last = []
    
    data.append(data_last)
    code = data

    return code
  
  def decode_2d(data):
    origin = []
    row = []
    col = []
    errorneous = False

    for i in range(len(data)):
        counts = data[i].count(1)
        if counts % 2 != 0:
            row.append(i)
            errorneous = True
    
    last = []
    line = 0
    for j in range(len(data[0])):
        for l in range(len(data)):
            last.append(data[l][j])
        counts = last.count(1)
        last = []
        if counts % 2 != 0:
            col.append(line)
            errorneous = True
        line += 1
    print("row: ", row)
    print("col: ", col)
    
    if errorneous == False:
        print("No Error Detected")
        return data
    num_err = len(row) * len(col)
    if num_err > 1:
        print("More than 1 bit error detected. Unable to fix the error.")
        return origin

    if data[row[0]][col[0]] == 0:
        data[row[0]][col[0]] = 1
    else:
        data[row[0]][col[0]] = 0
    print("1 bit error detected @ ", row, col)
    origin = data

    return origin
  
data = encode_2d([[1,0,0,0,1,1,1],[1,0,0,1,1,1,0],[1,0,0,0,0,0,0],[0,0,0,0,1,1,0]])
print(data)
print(decode_2d(data))

#2D parity test1
data = encode_2d([[1,0,0,0,1],[1,0,0,1,1],[1,0,0,0,0],[0,0,0,0,1]])
print(data)
data[0][3] ^= 1
data[2][2] ^= 1
#data[2][3] ^= 1
print(decode_2d(data))

#2D parity test2
data = encode_2d([[1,0,0,0,1],[1,0,0,1,1],[1,0,0,0,0],[0,0,0,0,1]])
print(data)
data[0][3] ^= 1
print(decode_2d(data))
