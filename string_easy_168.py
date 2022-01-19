def convertToTitle(columnNumber):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if (columnNumber <= 26): return alpha[columnNumber-1]
    
    if (columnNumber % 26 == 0): 
        return convertToTitle(columnNumber//26-1) + alpha[columnNumber%26-1]
    else:
        return convertToTitle(columnNumber//26) + alpha[columnNumber % 26-1]

print(convertToTitle(1))
print(convertToTitle(28))
print(convertToTitle(701))
print(convertToTitle(52))