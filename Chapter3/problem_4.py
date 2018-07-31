# 3.4
# Implement a queue class using two stacks

class QueueStack:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def add(self, val):
        self.stack1.append(val)

    def dequeue(self):
        if not self.stack2:
            while (self.stack1):
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
