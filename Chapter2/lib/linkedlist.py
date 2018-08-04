class LinkedList:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = Node(data)

        else:
            curr = self.root
            while(curr.next):
                curr = curr.next
            curr.next = Node(data)

    def __str__(self):
        dataString = []
        current = self.root
        while (current):
            dataString.append(str(current.data))
            current = current.next
        return ' -> '.join(dataString)

class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
