#2,3,5,7,11,13,11,11,13
#            -        -

def remove_dup(nums):
    if len(nums) < 3:
        return nums
    
    i, j =1,2

    while j < len(nums):
        if nums[i] == nums[i - 1]:
            while j < len(nums) - 1 and nums[i] == nums[j]:
                j += 1
            nums[i] = nums[j]
        i += 1
        j += 1
    
    return nums

if __name__ == "__main__":
    nums = [2,3,5,5,7,11,11,11,13]
    print(remove_dup(nums))

    nums = [2,2]
    print(remove_dup(nums))

    nums = [1,2,3,4,5,6,7]
    print(remove_dup(nums))
