from functools import lru_cache

words_dict = {"leet", "code"}
s = "leetcode"
n = len(s)

@lru_cache
def word_break(start):
    if start == n:
        return True
    
    for end in range(start, n):
        if s[start:end + 1] in words_dict and word_break(end + 1):
            return True
        
    return False

print(word_break(0))


