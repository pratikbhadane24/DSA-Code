class Queue:
    def __init__(self, value):
        self.queue = []
        self.length = 0

    def enqueue(self, value):
        self.queue.append(value)
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        self.length -= 1
        return self.queue.pop(0)
