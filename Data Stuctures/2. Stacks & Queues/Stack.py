class MyStack:
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0

    def is_empty(self):
        return self.stack_size == 0

    def peek(self):
        return self.stack_list[-1]

    def size(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.stack_size
    
    def push(self, element):
        self.stack_size += 1
        self.stack_list.append(element)
        return

    def pop(self):
        if self.is_empty():
            return None
        self.stack_size -= 1
        return self.stack_list.pop()
        