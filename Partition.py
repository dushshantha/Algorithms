'''
Partition a linkedList based on x where all elements less than x appear left of the list
'''

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def populateLinkedList(a):
    head, tail = None, None
    if not a:
        return None
    head = Node(a[0])    
    tail = head
    for i in range(1, len(a)):
        tail.next = Node(a[i])
        tail = tail.next
    
    return head



def printList(l):
    curr = l
    while curr:
        print(curr.val, end =" ")
        curr = curr.next
    print()


def partition(l, x):
    if l == None:
        return None

    beforeHead, beforeTail = None, None
    afterHead, afterTail = None, None
    curr = l
    while curr:
        tmp = curr
        curr = curr.next
        tmp.next = None
        if tmp.val < x:
            if beforeHead:
                beforeTail.next = tmp
                beforeTail = beforeTail.next
            else:
                beforeHead = tmp
                beforeTail = beforeHead

        else:
            if afterHead:
                afterTail.next = tmp
                afterTail = afterTail.next
            else:
                afterHead = tmp
                afterTail = afterHead
    if beforeTail:
        beforeTail.next = afterHead
    else:
        beforeHead = afterHead
    return beforeHead
                

l = populateLinkedList([1])
printList(partition(l,0))

l = populateLinkedList([6,2,3,6,7,2,7])
printList(partition(l, 4))

l = populateLinkedList([1,1,1,1,1])
printList(partition(l, 1))




