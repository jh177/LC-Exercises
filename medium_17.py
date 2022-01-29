# # letter combinations of a phone number

def letterCombinations(self, digits: str):
    if len(digits) == 0: return []
    
    order = {
      "2":["a","b","c"],
      "3":["d","e","f"],
      "4":["g","h","i"],
      "5":["j","k","l"],
      "6":["m","n","o"],
      "7":["p","q","r","s"],
      "8":["t","u","v"],
      "9":["w","x","y","z"],
      }

    letters = []
    combos = []

    for n in digits:
        letters.append(order[n])
    
    while len(letters) > 0:
        chars = letters.pop(0)
        combos = self.getLetterCombos(combos, chars)
    
    return combos



def getLetterCombos(self, combos, chars):
    res = []
    for combo in combos:
        for char in chars:
            res.append(combo+char)
    return res






#     return result    
    