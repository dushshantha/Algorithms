def count3SumLessThan9(nums):
    count = 0
    if len(nums) < 3:
        return 0
    
    s = nums[0] + nums[1] + nums[2]
    if s < 9:
        count += 1
    
    i = 3

    while i < len(nums):
        s = s - nums[i - 3] + nums[i]
        if s < 9:
            count += 1
        i += 1
    
    return count



if __name__ == "__main__":
    nums = [1,4,3,5,4,6,7,1,0] 
    print(count3SumLessThan9(nums))

