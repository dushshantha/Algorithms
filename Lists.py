class Node:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

def reverse(L):
    new_List = None
    if not L:
        return None

    while L:
        temp = L
        L = L.next
        temp.next = new_List
        new_List = temp

    return new_List

def print_list(L):
    while L:
        print(L.data)
        L = L.next

if __name__ == '__main__':
    L = Node(data = 0)

    tail = L
    for i in range(1,7):
        tail.next = Node(data=i)
        tail = tail.next

    print_list(L)

    s = reverse(L)
    print_list(s)
