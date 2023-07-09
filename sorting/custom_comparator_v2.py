from functools import cmp_to_key

# -1 means ordering of elements didn't change (ele1 comes before ele2)
# 1 means ordering of elements reversed (ele2 comes before ele1)

# Custom comaprator to sort a list in reverse order
def comparator(ele1, ele2):
    print(f"ele1 = {ele1}, ele2 = {ele2}")
    if ele1 < ele2:
        return 1 # ele2 comes before ele1
    
    else:
        return -1 # ele1 comes before ele2

nums = [3,30,34,5,9]
comparator_key = cmp_to_key(comparator)
nums.sort(key = comparator_key)
print(nums)