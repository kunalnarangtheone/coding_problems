def substrings_with_one_repeating(s, k):
    n = len(s)
    counter = [0] * 26
    res = []

    if k > n:
        return []
    
    counter_with_repeating = 0

    for i in range(k):
        counter[ord(s[i]) - ord("a")]+=1
        if counter[ord(s[i]) - ord("a")] > 1:
            counter_with_repeating+=1

    if counter_with_repeating == 1:
        res.append(s[:k])

    for i in range(k, n):
        if counter[ord(s[i - k]) - ord("a")] > 1:
            counter_with_repeating-=1

        counter[ord(s[i - k]) - ord("a")]-=1
        counter[ord(s[i]) - ord("a")]+=1

        if counter[ord(s[i]) - ord("a")] > 1:
            counter_with_repeating+=1

        if counter_with_repeating == 1:
            res.append(s[i - k + 1:i + 1])

    return res

print(substrings_with_one_repeating("awaglk", 4))


    

