'''
Having a list of integers, we want to know if we can split it evenly in two parts.
'''

def canPartition2(array):
    total = sum(array)

    if total % 2:
        return False

    half = total // 2

    memo = [[False] * (len(array) +1) for _ in range(half + 1)]

    for i in range(1, half + 1):
        for j in range(1, len(array) + 1):
            if i == array[j - 1] or memo[i][j -1]:
                memo[i][j] = True
            else:
                diff = i - array[j - 1]
                if diff > 0 and memo[diff][j - 1]:
                    memo[i][j] = True
    return memo[i][j]

assert(canPartition2([3,1,1,2,2,1]))