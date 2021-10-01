def array_front9(nums):
    end = len(nums)
    if end > 4:
        end = 4

    count = 0
    for i in range(end):
        if nums[i] == 9:
            count += 1
            break

    if count == 1:
        return True
    else:
        return False


a = array_front9([1, 9, 7, 5, 5, 8])
print(a)