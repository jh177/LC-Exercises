def strStr(haystack, needle):
    if needle == "": return 0
    length = len(needle)

    for i in range(len(haystack)):
        if haystack[i:i+length] == needle: return i
    
    return -1

print(strStr("hello", "ll"))
print(strStr("hello", "lla"))
print(strStr("hello", "lo"))
print(strStr("hello", ""))
print(strStr("", "a"))
print(strStr("", ""))