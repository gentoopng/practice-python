nums = list(map(int, input().split()))
index = 0
for i in nums:
    if nums[index] == 0:
        print(index+1)
    index += 1