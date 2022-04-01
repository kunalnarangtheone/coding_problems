from collections import defaultdict
def uniqueLetterString(s: str) -> int:
    """
    The key ideas behind the solution:
    1. The maximum possible substrings that can end at an index are i + 1.
    2. The contribution of a character to this substring is (i + 1) - it's last seen position.
    3. At each point, sum of all contributions, gives the number of total substrings found so far.
    4. The last seen position of char is actually i + 1.
    """
    last_position = defaultdict(int) # Used for storing the last position of each character, so the size
    # exceeds 26
    contribution = defaultdict(int) # Used for storing the contribution of each character so far, it's
    # size also never exceeds 26. This will possibly be updated throughout the string traversal.
    res = 0

    for i, char in enumerate(s):
        max_possible_substrs_at_idx = i + 1
        contribution[char] = max_possible_substrs_at_idx - last_position[char]

        res+=sum(contribution.values())
        last_position[char] = i + 1

    return res

print(uniqueLetterString("ABCB"))
