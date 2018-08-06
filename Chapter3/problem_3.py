# Problem 2.3) Implement a stack as a set of stacks. When one stack reaches a
# stack height it will create a new stack to hold the new data.

# Thoughts
# Major modifications to the push and pop operation.

# For push we need to check if we are at the end of a stack, create a new one
# and place it at the beginning of that stack.

# For pop we need to check if we are at the beginning of a stack. If so we need
# to pop the element and the substack itself from the mainstack.
# - If the stack is empty then we need to raise an error



class SetOfStacks:
    STACK_HEIGHT = 5

    def __init__(self):
        self.stackset = []

    def push(self, data):
        if not self.stackset or \
        len(self.stackset[len(self.stackset) - 1]) == self.STACK_HEIGHT:
            self.stackset.append([data])
        else:
            self.stackset[len(self.stackset) - 1].append(data)

    def pop(self):
        if not self.stackset:
            raise BufferError
        else:
            ret = self.stackset[len(self.stackset) - 1].pop()
            if not self.stackset[len(self.stackset) - 1]:
                self.stackset.pop()
            return ret

    def peek(self):
        return self.stackset[len(self.stackset) - 1].peek()
