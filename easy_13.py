# roman to integer
# make a dictionary for [I, V, X, L, C, D, M]
# iterate through s, if next char ranks higher, do the subtract


def romanToInt(s):
  rank = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
  result = 0
  i = 0
  while i < len(s):
    if i+1 < len(s) and rank[s[i]] < rank[s[i+1]]:
      result += rank[s[i+1]] - rank[s[i]]
      i += 2
    else:
      result += rank[s[i]]
      i += 1
  return result