from tabnanny import check


def groupAnagrams(strs):
    checked = {}

    for str in strs:
        sorted_str = "".join(sorted(str))
        if sorted_str in checked:
            checked[sorted_str].append(str)
        else:
            checked[sorted_str] = [str]

    return checked.values()


def isAnagram(str1, str2):
    if len(str1) != len(str2):
        return False
    
    sorted_str1 = "".join(sorted(str1))
    sorted_str2 = "".join(sorted(str2))

    return sorted_str1 == sorted_str2
    # char_count = {}

    # for char in str1:
    #     if char not in char_count:
    #         char_count[char] = 1
    #     else:
    #         char_count[char] += 1

    # for char in str2:
    #     if char not in char_count:
    #         return False
    #     else:
    #         char_count[char] -= 1

    # for k,v in char_count.items():
    #     if v != 0: return False

    # return True


# strs = ["eat","tea","tan","ate","nat","bat"]
strs = ["", "b", ""]
print(groupAnagrams(strs))
