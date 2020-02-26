def selectionSort(a):
    for i in range(len(a)):
        minIndex = i
        for j in range(i, len(a)):
            if a[minIndex] > a[j]:
                minIndex = j
        
        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp

    return a

print(selectionSort([3,5,2,3,1,4,6]))
print(selectionSort([]))
print(selectionSort([1,1,1,1,1,1,1,1,1]))
