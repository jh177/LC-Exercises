# 242. Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

def is_anagram(s,t)
  return false if s.length != t.length
  s.each_char {|char| t[t.index(char)] = "" if t.include?(char)}
  t.empty?
end

s = "anagram"
t = "nagaram"
p is_anagram(s,t)