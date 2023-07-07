nums = [1, -5, 6, 2]

curr = maxx = nums[0]

for num in nums[1:]:
    curr = max(0, curr) + num
    maxx = max(maxx, curr)

print(maxx)