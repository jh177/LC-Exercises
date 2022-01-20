def isIsomorphic(s, t):
    if len(s) != len(t): return False
    char = {}
    checked = set()
    for i in range(len(s)):
        if s[i] not in char:
            if t[i] in checked:
                return False
            else:
                char[s[i]] = t[i]
                checked.add(t[i])
        else:
            if t[i] != char[s[i]]:
                return False

    return True


print(isIsomorphic("egg", "add"))
print(isIsomorphic("egg", "adc"))
print(isIsomorphic("egg", "ac"))
print(isIsomorphic("paper", "title"))
print(isIsomorphic("babc", "dada"))