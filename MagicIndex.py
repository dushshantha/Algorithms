'''
A magic index in an array is such that A[i] = i. Find a mgic index in a sorted array of distinct integers if any.

what if elements are not distinct?

'''

def findMagicIndex_Distinct(A):
    return magicRec(A, 0, len(A) - 1)

def magicRec(l, s, e):   # [-1,1,5,6,8] 1, 1  mid = 1 + 1//2 = 1
                         #   -    
    if s > e:
        return -1
    
    mid = (s + e) //2

    if l[mid] == mid:
        return mid
    
    elif l[mid] > mid:
        return magicRec(l, s, mid - 1)
    else:
        return magicRec(l, mid+1, e)

A = [-1, 1, 5, 6, 8]
print(findMagicIndex_Distinct(A))
B = [0]
print(findMagicIndex_Distinct(B))
C = [1,1,1,1,1]
print(findMagicIndex_Distinct(C))
D = [5,6,7,8,9]
print(findMagicIndex_Distinct(D))
E = [-1,0,1, 3,6]
print(findMagicIndex_Distinct(E))