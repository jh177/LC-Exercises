# get shortest element
# iterater through shortest element and list

def longestCommonPrefix(strs):
  strs.sort(key=len)
  shortest_str = strs[0]
  longest = ""

  for i in range(len(shortest_str)):
    for str in strs:
      if shortest_str[:i+1] not in str[:i+1]:
        return longest
    longest = shortest_str[:i+1]
  
  return longest


