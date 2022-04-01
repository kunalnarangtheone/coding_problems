import math

# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# nums = [5, 4, -1, 7, 8]
nums = [1]

summ, maxx = 0, -math.inf
start = end = 0

for i, num in enumerate(nums):
    if summ == 0:
        start = end = i
    summ+=num

    if maxx <= summ:
        maxx = summ
        end = i

    if summ < 0:
        summ = 0
        start = end = i

print(f"Maximum subarray sum: {maxx}")
print(f"Start: {start}, End = {end}")
print(f"Numbers: {nums[start: end + 1]}")
