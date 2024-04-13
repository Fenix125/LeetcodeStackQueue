class Queue:
    def __init__(self, data= None) -> None:
        self.data = data
        self.next = None
    def push(self, x):
        if self.data is None:
            self.data = x
        else:
            curr = self
            while curr.next is not None:
                curr = curr.next
            curr.next = Queue(x)
    def peek(self):
        return self.data
    def pop(self):
        popped = Queue(self.data)
        if self.next is None:
            self.data = None
            return popped.data
        self.data = self.next.data
        self.next = self.next.next
        return popped.data
    def empty(self):
        if self.data is None:
            return True
        return False
