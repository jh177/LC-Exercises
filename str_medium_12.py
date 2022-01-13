# integer to roman
# make a dictionary for [I, V, X, L, C, D, M]
# divide number by 10 --> check if it is a 4 or 9
# divide residule by 10


def intToRoman(num):
  rank = {
    1: "I", 2: "II", 3: "II", 4:"IV", 5: "V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX", 
    10: "X", 20: "XX", 30: "XXX", 40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC",
    100: "C", 200: "CC", 300: "CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC", 800: "DCCC", 900: "CM",
    1000: "M", 2000: "MM", 3000: "MMM",}
  result = ""

  while num > 10:
    remainder = 0
    if num%1000 != num:
      remainder = num % 1000
    elif num% 100 !=num:
      remainder = num % 100
    else:
      remainder = num % 10
    num = num - remainder
    result += rank[num]
    num = remainder

  if (num!=0): result += rank[num]

  return result

print(intToRoman(1994))