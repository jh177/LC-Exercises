def lengthOfLastWord(s):
    words = s.split()
    return len(words[-1])


print(lengthOfLastWord("luffy is still joyboy"))
