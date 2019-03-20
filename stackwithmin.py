class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class stack:
    def __init__(self, head = None):
        self.head = head
        self.min = head
        self.preMin = None
    
    def push(self, newNode):
        if newNode.data < self.min.data:
            self.preMin = self.min
            self.min = newNode

        newNode.next = self.head
        self.head = newNode

    def pop(self):
        ret = self.head
        if self.head ==  self.min:
            self.min = self. preMin
        self.head = self.head.next
        ret.next = None
        return ret



