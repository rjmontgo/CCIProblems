class MinStackNode:
    def __init__(self, data=None, min=None):
        self.data = data
        self.min = min

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        if not self.stack or data < self.min():
            self.stack.append(MinStackNode(data, data))
        else:
            self.stack.append(MinStackNode(data, self.min()))

    def peek(self):
        return self.stack[-1]

    def min(self):
        return self.peek().min

    def pop(self):
        return self.stack.pop()
