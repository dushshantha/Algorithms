class node:
    def __init__(self, data= 0, next = None):
        self.data = data
        self.next = next
    
def evenOddMerger(L):

    if not L:
        return None

    temp = tail = None
    curr = L
    while curr.next:
        if not temp:
            temp = tail = curr.next
        else:
            tail.next = curr.next
            tail = tail.next

        curr.next = tail.next
        if curr.next:
            curr = curr.next
        tail.next = None
    
    curr.next = temp
    return L

def printL(L):
    while L:
        print(L.data)
        L = L.next


if __name__ == "__main__":
    L = node(data=0)
    temp = L
    for i in range(1,6):
        temp.next = node(data=i)
        temp = temp.next
    
    printL(L)
    printL(evenOddMerger(L))  

    