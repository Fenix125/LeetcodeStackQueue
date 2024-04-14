class CustomDict:
    def __init__(self, data= None) -> None:
        self.data = data
        self.freq = 0
        self.next = None
    def push(self, val: int):
        if self.data is None:
            self.data = val
            self.freq += 1
        else:
            previous = None
            curr = self
            try:
                while curr.data != val:
                    previous = curr
                    curr = curr.next
                curr.freq += 1
            except AttributeError:
                previous.next = CustomDict(val)
                previous.next.freq += 1
                
    def pop(self):
        pass


class FreqStack:
    def __init__(self, data= None):
        self.data = data
        self.next = None 
        self.dict_freq = CustomDict()
    def push(self, val: int) -> None:
        self.dict_freq.push(val)
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
    
cust_dict = CustomDict()
cust_dict.push(1)
cust_dict.push(2)
cust_dict.push(1)