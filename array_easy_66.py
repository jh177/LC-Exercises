# plus one
def plusOne(digits):
    i = len(digits)-1
    num = 0

    while i >= 0:
        num += digits[i] * (10 ** (len(digits)-i-1))
        i -= 1

    print(num)
    num += 1

    num_str = str(num)
    digits_str = list(num_str)

    result = map(lambda x: int(x), digits_str)

    return result


print(plusOne([4, 3, 2, 1]))

