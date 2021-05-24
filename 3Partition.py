def canPartition3(array):
    total = sum(array)

    if total % 3:
        return False
    
    part = total // 3

    memo = [ [0] * (len(array) + 1) for _ in range(part + 1)]

    for i in range(1, part + 1):
        for j in range(1, len(array) + 1):
            diff = i - array[j - 1]
            if array[j - 1] == i or (diff > 0 and memo[diff][j -1]):
                memo[i][j] = 1 if memo[i][j - 1] == 0 else 2
            else:
                memo[i][j] = memo[i][j - 1]
    return True if memo[i][j] == 2 else False

assert(canPartition3([3,1,1,2,2]))