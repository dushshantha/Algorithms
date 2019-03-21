class Node:
    def __init__(self, data, next = None, min = None):
        self.data = data
        self.next = next
        self.min = min

class stack:
    def __init__(self, head = None):
        self.head = head
        self.head.min = head

    def push(self, newNode):
        if newNode.data < self.head.min.data:
            newNode.min = newNode
        else:
            newNode.min = self.head.min

        newNode.next = self.head
        self.head = newNode

    def pop(self):
        ret = self.head
        self.head = self.head.next
        ret.next = None
        return ret

    def getmin(self):
        return self.head.min



if __name__ == '__main__':
    s = stack(Node(data = 5))
    s.push(Node(data = 6))
    s.push(Node(data = 3))
    s.push(Node(data = 4))

    print(s.getmin().data == 3)
    s.pop()
    print(s.getmin().data == 3)
    s.pop()
    print(s.getmin().data == 5)
