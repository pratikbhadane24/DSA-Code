class Stack:
    def __init__(self):
        self.stack = []
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        return self.length

    def push(self, value):
        self.stack.append(value)
        self.length += 1
        
    def pop(self):
        if self.is_empty():
            return None
        self.length -= 1
        return self.stack.pop()