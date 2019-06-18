'''
pairs of numbers that form the n sum
'''

def sums(nums, n):
    dp = []
    pairs = []
    
    nums.sort()
    #nums = set(nums)

    for i in nums:
        if n - i in dp :
            if not [i, n - i] in pairs:
                pairs.append([i, n - i])
        
        dp.append(i)
    return pairs

if __name__ == "__main__":
    nums = [1,2,5,4,6,7,3,4,6,8,7,9,3,4]
    num = 6

    print(sums(nums, 6))