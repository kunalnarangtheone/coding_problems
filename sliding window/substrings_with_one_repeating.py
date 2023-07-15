from collections import defaultdict
def substrings(s, k):
    n = len(s)

    if k > n:
        return []

    freq_with_more_than_one_repeating = 0
    lookup = defaultdict(int)
    ans = set()
    
    for i in range(k):
        lookup[s[i]]+=1
        if lookup[s[i]] > 1:
            freq_with_more_than_one_repeating+=1

        if freq_with_more_than_one_repeating == 1:
            ans.add(s[:k])

    for i in range(k, n):
        if lookup[s[i - k]] > 1:
            freq_with_more_than_one_repeating-=1

        lookup[s[i - k]]-=1
        lookup[s[i]]+=1

        if lookup[s[i]] > 1:
            freq_with_more_than_one_repeating+=1

        if freq_with_more_than_one_repeating == 1:
            ans.add(s[i - k + 1: i + 1])

    return list(ans)

print(substrings("awaglk", 4))