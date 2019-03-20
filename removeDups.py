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


def removeDups(l):
    mem = []
    mem.append(l.val)
    curr = l
    while curr.next:
        print(curr.next.val)
        print(mem) 
        if curr.next.val in mem:
            curr.next = curr.next.next
        else:
            mem.append(curr.next.val)
            curr = curr.next
    return l

def printKthToLast(l, k):
    curr = l
    ret = None
    for i in range(k):
        if not curr:
            return None 
        curr = curr.next
    ret = l
    while curr:
        curr = curr.next
        ret = ret.next
    
    print(ret.val)

def deleteNode(n):
    n.val = n.next.val
    n.next = n.next.next


     

if __name__ == "__main__":
    l = populateLinkedList([4,3,4,6,5,7,6,5,5,9,8])
    printList(l)
    printList(removeDups(l))
    printKthToLast(l, 3)
