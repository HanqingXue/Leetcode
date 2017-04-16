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


class Solution(object):
    def __init__(self):
        self.match = {'}': '{', ']': '[', ')': '('}
        self.left = ['(', '{', '[']
        self.right = ['}', ']', ')']
        self.stack = Stack()
    
    def isValid(self, s):
        if len(s) % 2 == 1: return False
        
        for alpha in s:
            if alpha in self.left:
                self.stack.push(alpha)
            elif alpha in self.right:
                if self.stack.isEmpty(): return False
                match_alpha = self.match[alpha]
                peek = self.stack.peek()
                if peek == match_alpha:
                    self.stack.pop()
            else:
                continue
        
        if self.stack.size() == 0:
            return True
        else:
            return False
        
        return False

