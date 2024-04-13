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
    
class MyStack:
    def __init__(self):
        self.head = Queue()
        self.tail = Queue()
    def push(self, x: int) -> None:
        while self.head.data is not None:
            popped_head = self.head.pop()
            self.tail.push(popped_head)
        self.tail.push(x)
        while self.tail.data is not None:
            popped_tail = self.tail.pop()
            self.head.push(popped_tail)

    def pop(self) -> int:
        return self.head.pop()

    def top(self) -> int:
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        return curr.data

    def empty(self) -> bool:
        if self.head.data is None:
            return True
        return False
 

stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())
print(stack.pop())
print(stack.empty())
