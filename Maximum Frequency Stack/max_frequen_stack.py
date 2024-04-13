class FreqStack:
    def __init__(self, data= None):
        self.data = data
        self.next = None 
    def push(self, val: int) -> None:
        if self.data is None:
            self.data = val
        else:
            curr = self
            while curr.next != None:
                curr = curr.next
            curr.next = FreqStack(val)
    def pop(self) -> int:
        if self.next is None:
            popped = FreqStack(self.data)
            self.data = None
            return popped.data
        curr = self
        while curr.next.next is not None:
            curr = curr.next
        popped = FreqStack(curr.next.data)
        curr.next = None
        return popped.data