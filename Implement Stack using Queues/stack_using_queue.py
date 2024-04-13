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
        self.head.push(x)
    def pop(self) -> int:
        while self.head.next is not None:
            self.tail.push(self.head.pop())
        popped = self.head.pop()
        self.head, self.tail = self.tail, self.head
        return popped

    def top(self) -> int:
        while self.head.next is not None:
            self.tail.push(self.head.pop())
        element = self.head.data
        self.tail.push(self.head.pop())
        self.head, self.tail = self.tail, self.head
        return element

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
print(stack.top())
