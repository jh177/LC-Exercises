def isPalindrome(s):
    word = ""
    for char in s:
        if char.isalnum(): word += char
    
    word = word.lower()

    i = 0
    j = len(word)-1

    while i <= j:
        if word[i] != word[j]: return False
        i += 1
        j -= 1

    return True

print(isPalindrome("race a car"))
print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome(" "))
