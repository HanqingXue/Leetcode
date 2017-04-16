class Stack(object):
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.stack == []:
            raise IndexError('pop from empty stack')
        else:
            del self.stack[-1]
    
    def top(self):
        return self.stack[-1]
    
    def peek(self):
        return self.stack[-1]
    
    def size(self):
        return self.stack.__len__()
    
    def isEmpty(self):
        return True if self.stack == [] else False
