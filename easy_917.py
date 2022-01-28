def reverseOnlyLetters(s):
    chars = list(s)
    l = 0
    r = len(s)-1

    while l < r:
        if chars[l].isalpha() and chars[r].isalpha():
            chars[l], chars[r] = chars[r], chars[l]
            l += 1
            r -= 1
        elif chars[l].isalpha() and not chars[r].isalpha():
            r -= 1
        elif not chars[l].isalpha() and chars[r].isalpha():
            l += 1
        else:
            l += 1
            r -= 1
    
    return "".join(chars)


s = "7_28]"
print(reverseOnlyLetters(s))
