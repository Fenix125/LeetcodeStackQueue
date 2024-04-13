class Stack:
    def __init__(self, data= None) -> None:
        self.data = data
        self.next = None
    def push(self, x):
        if self.data is None:
            self.data = x
        else:
            curr = self
            while curr.next != None:
                curr = curr.next
            curr.next = Stack(x)
    def pop(self):
        popped = self.data
        if self.next is None:
            self.data = None
            return popped
        curr = self
        while curr.next.next is not None:
            curr = curr.next
        curr.next = None
    def peek(self):
        curr = self
        while curr.next is not None:
            curr = curr.next
        return curr.data
    def empty(self):
        if self.data is None:
            return True
        return False
