def array123(nums):
    count = 0
    for i in range(len(nums) - 2):
        if [nums[i], nums[i+1], nums[i+2]] == [1, 2, 3]:
            count += 1
            break
    if count == 1:
        return True
    else:
        return False

x = array123([1, 2, 3, 2, 2, 3])
print(x)