def combinationSum(nums, target):
    cache = [[] * target]
    ret = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                partialSum = nums[i] + nums[j] + nums[k]
                if partialSum <= target:
                    cache[partialSum] = [nums[i] , nums[j] , nums[k]]

    for a in nums:
        if len(cache[target - a])

if __name__ == '__main__':
    main()
