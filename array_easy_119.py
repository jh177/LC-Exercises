def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1, 1]

    pascal = [[1], [1, 1]]

    while len(pascal) < rowIndex+1:
        pre_row = pascal[-1]
        next_row = [1]
        for i in range(len(pre_row)-1):
            next_row.append(pre_row[i] + pre_row[i+1])
        next_row += [1]
        pascal.append(next_row)

    return pascal[-1]


print(getRow(3))
print(getRow(4))
print(getRow(5))
