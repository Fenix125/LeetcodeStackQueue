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
        if self.next is None:
            popped = Stack(self.data)
            self.data = None
            return popped.data
        curr = self
        while curr.next.next is not None:
            curr = curr.next
        popped = Stack(curr.next.data)
        curr.next = None
        return popped.data
    def peek(self):
        curr = self
        while curr.next is not None:
            curr = curr.next
        return curr.data
    def empty(self):
        if self.data is None:
            return True
        return False
    def __str__(self) -> str:
        string = ''
        curr = self
        while curr is not None:
            string += ' ' + str(curr.data) + ' '
            curr = curr.next
        return string
class MyQueue:
    def __init__(self):
        self.head = Stack()
        self.tail = Stack()

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

    def peek(self) -> int:
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        return curr.data

    def empty(self) -> bool:
        if self.head.data is None:
            return True
        return False


    
queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.pop())
print(queue.peek())

