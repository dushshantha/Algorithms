def removeRepeatedNums(nums):
    i, j = 0,1
    ret = []
    l = len(nums) # 8

    # 1,2,2,3,3,3,1,1
    #                  -  -
    if l <= 1:
        return nums

    while i < l and j < l:
        if nums[i] != nums[j]:
            ret.append(nums[i]) # [1,2,2,1,1]
            i += 1
            j += 1
        
        else:
            while j < l and nums[i] == nums[j]:
                j += 1
            if j - i >= 3: # ignore all before j
                i = j
                j += 1

            else:
                while i < l and i < j:
                    ret.append(nums[i])
                    i += 1
                j += 1
    
    return ret



if __name__ == "__main__":
    print(removeRepeatedNums([3,1,2,2,2,1,1,1,2,2,3,1,1,2,2,2,1,1,1,2,3]))
    print(removeRepeatedNums([1,2,2,3,3,3,1,1]))
    print(removeRepeatedNums([1,1,1,3,3,3,1,1]))
    print(removeRepeatedNums([1]))
    print(removeRepeatedNums([]))