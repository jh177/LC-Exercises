require "byebug"

# 1347. Minimum Number of Steps to Make Two Strings Anagram

# Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.
# Return the minimum number of steps to make t an anagram of s.

# An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

# Example 1:

# Input: s = "bab", t = "aba"
# Output: 1
# Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

def min_steps(s,t)
  count = 0
  s.each_char.with_index do |char, i|
    if t.include?(char)
      count += 1
      t[t.index(char)] = ""
    end
  end
  return s.length - count
end

s = "anagram"
t = "mangaar"
p min_steps(s,t)