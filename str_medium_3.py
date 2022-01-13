# two pointer i, j
# j moves forward until s[i:j] includes s[j+1]
# compare s[i: j+1] with longest, max_len = len(longest)
# then i+=1, j = i+max_len
# then if s[i:j] to set length not equal to j-i, i+=1, j+=1
# else: j+=1 until s[i:j] includes s[j+1]

def lengthOfLongestSubstring(s):
  """
    :type s: str
    :rtype: int
    """
  i = 0
  j = 0

  max_len = 0

  while j < len(s):
    if j==len(s)-1 or s[j+1] in s[i:j+1]: 
      if len(set(s[i:j+1])) == j-i+1 and j-i+1 > max_len:
        max_len = j+1-i
      i += 1
      j = i + max_len
    elif len(set(s[i:j+1])) != j-i+1:
      i += 1
    else:
      j += 1
  
  return max_len


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))