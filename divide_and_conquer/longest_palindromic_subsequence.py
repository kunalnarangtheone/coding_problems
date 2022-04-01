import math

def lps(s, index1, index2):
    if index1 > index2:
        return ""

    elif index1 == index2:
        return s[index1]

    elif s[index1] == s[index2]:
        return s[index1] + lps(s, index1 + 1, index2 - 1) + s[index2]

    else:
        opt1 = lps(s, index1 + 1, index2)
        opt2 = lps(s, index1, index2 - 1)

        return opt1 if len(opt1) >= len(opt2) else opt2

s = "abcdba"
print(lps(s, 0, len(s) - 1))
