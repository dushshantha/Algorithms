'''
Given an array of numbers, return true if any subset sum up to the number given.
'''

def subsetSum(nums, n):
    nums.sort()
    dp = [[False for y in range(n + 1)] for x in range(len(nums))]
    #print(dp)
    for i in range(len(nums)):
        dp[i][0] = True # Zero
        for j in range(1, len(dp[i]),1):
            print(nums[i], j)
            if nums[i] == j: 
                
                dp[i][j] = True
                print(dp[i][j])
            elif i > 0 and (dp[i-1][j] or dp[i-1][j - nums[i]]):
                   dp[i][j] = True
    for l in dp:
        print(l) 


if __name__ == "__main__":
    nums = [1,2,5,4,6,7,3,4,6,8,7,9,3,4]
    num = 100
    subsetSum(nums, num)