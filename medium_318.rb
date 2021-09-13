# 318. Maximum Product of Word Lengths

# Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

 

# Example 1:

# Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".
# Example 2:

# Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4
# Explanation: The two words can be "ab", "cd".
# Example 3:

# Input: words = ["a","aa","aaa","aaaa"]
# Output: 0
# Explanation: No such pair of words.

def max_product(words)
  longest = 0
  words.each_with_index do |word, i|
    uniques = words[i+1..-1]
    word.each_char do |char|
      uniques.reject! {|unique| unique.include?(char)}
    end
    if !uniques.empty?
      product = uniques.max_by(&:length).length * word.length
      longest = product if product > longest
    end
  end
  longest
end


words1 = ["abcw","baz","foo","bar","xtfn","abcdef"]
words2 = ["a","ab","abc","d","cd","bcd","abcd"]
words3 = ["a","aa","aaa","aaaa"]

p max_product(words1)
p max_product(words2)
p max_product(words3)