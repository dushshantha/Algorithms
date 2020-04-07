heap = [0]

def getParent(i):
    return (i - 1) // 2



def siftUp(i, heap):
    curr = i
    p = getParent(i)
    while p >= 0 and heap[p] < heap[curr]:
        #print(p, curr)
        tmp = heap[p]
        heap[p] = heap[curr]
        heap[curr] = tmp
        curr = p
        p = getParent(curr)
    print(heap)

def siftDown(i, heap):
    curr = i
    l = (curr * 2) + 1
    r = l + 1

    while l < len(heap):
        c = l
        if r < len(heap) and heap[l] < heap[r]:
            c = r
        
        if heap[curr] < heap[c]:
            tmp = heap[curr]
            heap[curr] = heap[c]
            heap[c] = tmp
            curr = c
            l = curr * 2
            r = l + 1
        else:
            break
    
    print(heap)

        
        
def extractMax(heap):

    if(len(heap) > 1):
        ret = heap[0]
        l = heap.pop()
        heap[0] = l
        siftDown(0, heap)
        return ret
    return heap.pop()

def insertHeap(heap, x):
    heap.append(x)
    siftUp(len(heap) - 1, heap)

def buildHeap(a):
    for i in range(getParent(len(a) - 1), -1 , -1):
        siftDown(i, a)
    

def heapSort(a):
    ret = []
    buildHeap(a)
    while a:
        ret.append(extractMax(a))
    return ret[::-1]

    

'''
h = [40,38,20,21,18,17,18,7,27]
siftUp(len(h) - 1, h)

h = [40,38,20,21,18,17,18,7,48]
siftUp(len(h) - 1, h)

h = [12,40,38,20,21,18,17,18,7,48]
siftDown(0, h)

h = [24,40,38,20,21,18,17,18,7,48]
siftDown(0, h)

h = [40,38,15,20,21,18,17,18,7,27]
siftDown(2, h)
siftDown(4, h)

h = [40, 38, 18, 20, 27, 15, 17, 18, 7, 21]
print(extractMax(h))
print(extractMax(h))
print(extractMax(h))
print(h)


h = [40, 38, 18, 20, 27, 15, 17, 18, 7, 21]
insertHeap(h, 28)
print(h)

h = [40, 38, 18, 20, 27, 15, 17, 18, 7, 21]
insertHeap(h, 50)
print(h)


h = [40, 38, 18, 20, 27, 15, 17, 18, 7, 21]
insertHeap(h, 4)
print(h)

'''

a = [2,3,5,4,7,6,2,3,5,4,7,6,8]
buildHeap(a)
print(a)


a = [2,3,5,4,7,6,2,3,5,4,7,6,8]
print(heapSort(a))


