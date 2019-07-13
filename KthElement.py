class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None


a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

def kth_to_last_node(k, a):

    far = a
    for i in range(k):
        if not far:
            return None
        far = far.next
    near = a

    while far:
        far = far.next
        near = near.next
    
    return near


# Returns the node with value "Devil's Food" (the 2nd to last node)
print(kth_to_last_node(2, a).value)
print(kth_to_last_node(3, a).value)

print(kth_to_last_node(6, a))