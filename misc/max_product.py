arr = [1, -5, -4, 3]

max_so_far = min_so_far = 1

for num in arr:
    tmp1 = max_so_far
    tmp2 = min_so_far

    max_so_far = max(num, num * tmp1, num * tmp2)
    min_so_far = min(num, num * tmp1, num * tmp2)

print(max_so_far)
