def binarySearch(l, s, e, v):
    print('in binary search')
    if s <= e:
        m = (s + e)//2
        if l[m] == v:
            return m
        if l[m] < v:
            return binarySearch(l, m + 1, e, v)
        if l[m] > v:
            return binarySearch(l, s, m - 1, v)
    else:
        return -1

def binarySearchLessThan(l, s, e, v):
    print('in binary search')
    if s <= e:
        if l[s] >= v:
            return s
        if l[e] < v:
            return e + 1
        m = (s + e)//2
        if l[m] == v:
            return m
        if l[m] < v:
            return binarySearch(l, m + 1 , e, v)
        if l[m] > v:
            return binarySearch(l, s, m -1, v)
    else:
        return -1

if __name__ == "__main__":
    l = [1,2,3,5,5,6]
    print(binarySearch(l, 0, len(l) - 1, 4))
    print(binarySearch(l, 0, len(l) - 1, 5))
    print(l[:binarySearchLessThan(l, 0, len(l) - 1, 4)])
    print(l[:binarySearchLessThan(l, 0, len(l) - 1, 5)])