def lcs(s1, s2, index1, index2):
    if index1 > len(s1) - 1:
        return ""

    elif index2 > len(s2) - 1:
        return ""

    elif s1[index1] == s2[index2]:
        return s1[index1] + lcs(s1, s2, index1 + 1, index2 + 1)

    else:
        opt1 = lcs(s1, s2, index1 + 1, index2)
        opt2 = lcs(s1, s2, index1, index2 + 1)

        return opt1 if len(opt1) >= len(opt2) else opt2

print(lcs("elephant", "erepat", 0, 0))
