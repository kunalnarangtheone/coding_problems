
def substrings(s, k):
    n = len(s)
    if k > n:
        return []
    
    ans = set()
    l = r = 0
    counter = dict()

    while r < n:
        counter[s[r]] = counter.get(s[r], 0) + 1
        uniq_count = len(counter)

        if r - l + 1 > k:
            counter[s[l]]-=1

            if counter[s[l]] == 0:
                del counter[s[l]]
                uniq_count-=1
            l+=1

        if uniq_count == k - 1:
            ans.add(s[l:r + 1])

        r+=1

    return list(ans)

# print(substrings("awaglk", 4))
print(substrings("aaaabcab", 3))