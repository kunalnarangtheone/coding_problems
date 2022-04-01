
def convert_string(s1, s2, index1, index2):
    if index1 == len(s1) - 1:
        return len(s2) - index2

    elif index2 == len(s2) - 1:
        return len(s1) - index1

    elif s1[index1] == s2[index2]:
        return convert_string(s1, s2, index1 + 1, index2 + 1)

    else:
        delete = 1 + convert_string(s1, s2, index1, index2 + 1)
        insert = 1 + convert_string(s1, s2, index1 + 1, index2)
        update = 1 + convert_string(s1, s2, index1 + 1, index2 + 1)
        return min(delete, insert, update)

print(convert_string("abc", "aecbd", 0, 0))
