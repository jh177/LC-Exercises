# 1. helper function to check if palindromic

# 2. two pointer i, j
# 

# j moves forward until s[i:j] includes s[j+1]
# compare s[i: j+1] with longest, max_len = len(longest)
# then i+=1, j = i+max_len
# then if s[i:j] to set length not equal to j-i, i+=1, j+=1
# else: j+=1 until s[i:j] includes s[j+1]

def longestPalindrome(s):
    n = len(s)

    start_idx = 0
    max_len = 0

    for i in range(n):
        length = max(max_length(s, i, i), max_length(s, i, i+1))
        if length > max_len:
            max_len = length
            start_idx = i - (length-1)//2
    
    return s[start_idx: start_idx+max_len]
            


def max_length(s, l, r):
    n = len(s)
    while l >= 0 and r < n and s[l] == s[r]:
        l -= 1
        r += 1
    return r - l - 1




print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
