def keyNum(str):
    keys = {
        "abc": "2",
        "def": "3",
        "ghi": "4",
        "jkl": "5",
        "mno": "6",
        "pqrs": "7",
        "tuv": "8",
        "wxyz": "9"
    }

    result= ""

    for char in str:
        for key in keys:
            if char in key: result += keys[key]

    return result