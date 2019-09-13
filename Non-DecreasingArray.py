'''
You are given an array of integers in an arbitrary order. Return whether or not it is possible to make the array non-decreasing by modifying at most 1 element to any value.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example:

[13, 4, 7] should return true, since we can modify 13 to any value 4 or less, to make it non-decreasing.

[13, 4, 1] however, should return false, since there is no way to modify just one element to make the array non-decreasing.

[4, 4, 4,8,9]
       -
'''

def nonDecreasingArray(nums):
    c = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            if i == 1 or nums[i] >= nums[i-2]:
                nums[i-1] = nums[i]
                c += 1
            else:
                nums[i] = nums[i-1]
                c += 1
    return c == 1

print(nonDecreasingArray([13, 4, 7]) == True)
print(nonDecreasingArray([13, 4, 1]) == False)
print(nonDecreasingArray([13, 4, 7, 8, 2]) == False)
print(nonDecreasingArray([13, 4, 7]) == True)
