
class Queue:
    def __init__(self):
        self.enq = []
        self.deq = []

    def enqueue(self, v):
        self.enq.append(v)

    def dequeue(self):
        if not self.deq:
            while self.enq:
                self.deq.append(self.enq.pop())
        
        if not self.deq:
            return None
        return self.deq.pop()

if __name__ == "__main__":
    test = [1,2,3,4,5]
    q = Queue()
    for i in test:
        q.enqueue(i)
    
    for i in range(len(test)):
        print(q.dequeue())