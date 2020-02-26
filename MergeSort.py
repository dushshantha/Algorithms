def mergeSort(a):
    if len(a) <= 1:
        return a
    mid = len(a)//2
    a1 = mergeSort(a[:mid])
    a2 = mergeSort(a[mid:])
    return merge(a1,a2)

def merge(a1, a2):
    ret = []
    while len(a1) > 0 and len(a2) > 0:
        if a1[0] <= a2[0]:
            ret.append(a1[0])
            a1.pop(0)
        else:
            ret.append(a2[0])
            a2.pop(0)
        
    if len(a1) == 0:
        ret += a2
    if len(a2) == 0:
        ret += a1

    return ret

print(mergeSort([3,5,2,3,1,4,6]))
print(mergeSort([]))
print(mergeSort([1,1,1,1,1,1,1,1,1]))
