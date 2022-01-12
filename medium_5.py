# 1. helper function to check longest palindromic starting from two pointers
# 2. loop through string and expand from index to check longest palindromic


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
