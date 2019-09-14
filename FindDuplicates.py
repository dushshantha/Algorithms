'''
Find duplicates in 2 lists

'''
def findDuplicates(l1,l2):
    i,j = 0,0
    ret = []
    while i < len(l1) and j < len(l2):       
        if j < len(l2) and l2[j] == l1[i]:
            ret.append(l1[i])
            i += 1
            j += 1
        elif l1[i] < l2[j]:
            i += 1
        else:
            j += 1
        
    return ret

print(findDuplicates([1,2,3,4,5],[3,4,5,6,7]) == [3,4,5])
print(findDuplicates([],[3,4,5,6,7]) == [])
print(findDuplicates([1,2,3,4,5],[3]) == [3])