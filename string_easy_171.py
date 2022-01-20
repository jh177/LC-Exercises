from turtle import title


def titleToNumber(columnTitle):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = 0

    for i in range(len(columnTitle)):
        result += (alpha.index(columnTitle[i]) + 1) * 26 ** (len(columnTitle)-i-1)
    
    return result

print(titleToNumber("A"))
print(titleToNumber("AB"))
print(titleToNumber("ZY"))