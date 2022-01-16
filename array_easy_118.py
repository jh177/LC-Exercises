def generate(numRows):
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1, 1]]
    
    result = [[1], [1, 1]]
    
    while len(result) < numRows:
        pre_row = result[-1]
        next_row = [1]
        for i in range(len(pre_row)-1):
            next_row.append(pre_row[i] + pre_row[i+1])
        next_row += [1]
        result.append(next_row)
    
    return result


print(generate(3))
print(generate(4))
print(generate(5))

