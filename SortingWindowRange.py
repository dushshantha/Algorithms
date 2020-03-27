'''
Given a list of numbers, find the smallest window to sort such that the whole list will be sorted. If the list is already sorted return (0, 0). You can assume there will be no duplicate numbers.

Example:
Input: [2, 4, 7, 5, 6, 8, 9]
Output: (2, 4)

'''

def sortingWindow(l):
    low, upper = 0, len(l) - 1

    while low < upper and l[low] < l[low + 1]:
        low += 1

    while upper > low and l[upper] > l[upper - 1]:
        upper -= 1
    
    if low == upper:
        return (0,0)

    maxN = l[low]
    minN = l[upper]
    i = low
    while i <= upper:
        maxN = max(maxN, l[i])
        i += 1
    j = upper
    while j >= low:
        minN = min(minN, l[j])
        j -= 1

    while low > 0 and l[low - 1] >= minN:
        low -= 1
    
    while upper < len(l) - 1 and l[upper + 1] <= maxN:
        upper += 1

    return (low, upper)




print(sortingWindow([2,4,7,5,6,8,9]))

print(sortingWindow([2,4,7,8,5,6,9,10]))

print(sortingWindow([2,4,5,6,7,8,9]))

print(sortingWindow([5,4,3,2,1]))

print(sortingWindow([1,2,3,4,5]))