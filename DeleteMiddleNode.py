
'''
Delete the center(ish) element of a linked list
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

def deleteMid(l):
    f = l
    s = l
    p  = None
    if f == None or f.next == None:
        return l

    while s:
        if s.next:
            p = f
            f = f.next
            s = s.next.next
        else:
            s = None
    
    if p != l:    
        p.next = f.next

    return l

printList(deleteMid(None))

l = populateLinkedList([1])
printList(deleteMid(l))

l = populateLinkedList([1,2])
printList(deleteMid(l))

l = populateLinkedList([1,2,3,4,5])
printList(deleteMid(l))

l = populateLinkedList([1,2,3,4,5, 6])
printList(deleteMid(l))