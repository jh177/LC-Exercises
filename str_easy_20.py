def isValid(s: str):
  parentheses = {'(':')', '{':'}', '[':']'}
  count = []
  for char in s:
    if char in parentheses:
      count.append(char)
    else:
      if len(count) == 0:
        return False
      elif parentheses[count[-1]] != char:
        return False
      else:
        count.pop()
  
  return len(count) == 0


print(isValid("()[]{}"))
