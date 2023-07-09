from functools import cmp_to_key

def custom_sort(ele1, ele2):
    print(f"Comparing {ele1} and {ele2}")
    ord1 = ele1 + ele2
    ord2 = ele2 + ele1

    if ord1 < ord2:
        return -1

    else:
        return 1

def sorting():
    letter_cmp_key = cmp_to_key(custom_sort)

    nums = [3,30,34,5,9]
    nums = [str(num) for num in nums]
    nums.sort(key = letter_cmp_key)

    return "0" if nums[0] == "0" else "".join(nums)

print(sorting())