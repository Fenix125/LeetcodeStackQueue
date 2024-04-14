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
    def frequency(self, val):
        curr = self
        while curr.data != val:
            curr = curr.next
        return curr.freq
    def most_frequency_and_top(self, curr_stack):
        top_len = 1
        max_freq = 0
        max_top_len = 0
        most_freq_value = None
        curr = curr_stack
        while curr is not None:
            if self.frequency(curr.data) >= max_freq:
                if top_len > max_top_len:
                    most_freq_value = curr.data
                    max_freq = self.frequency(curr.data)
                    max_top_len = top_len
            curr = curr.next
            top_len += 1
        return most_freq_value
        
class FreqStack:
    dict_freq = CustomDict()
    def __init__(self, data= None):
        self.data = data
        self.next = None 
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
        most_frequent_val = self.dict_freq.most_frequency_and_top(self)
        encounter = 0
        previous = None
        while curr:
            if curr.data == most_frequent_val:
                if (encounter + 1) == self.dict_freq.frequency(curr.data):
                    previous.next = curr.next
                    curr_dict = self.dict_freq
                    while curr_dict.data != most_frequent_val:
                        curr_dict = curr_dict.next
                    curr_dict.freq -= 1
                    return most_frequent_val
                else:
                    encounter += 1
                    curr = curr.next
            else:
                previous = curr
                curr = curr.next
    
freqStack = FreqStack()
freqStack.push(5)
freqStack.push(7)
freqStack.push(5)
freqStack.push(7)
freqStack.push(4)
print(freqStack.pop())
print('a')