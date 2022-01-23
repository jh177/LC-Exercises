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


# strs = ["eat","tea","tan","ate","nat","bat"]
strs = ["", "b", ""]
print(groupAnagrams(strs))
