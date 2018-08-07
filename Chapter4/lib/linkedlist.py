class LinkedList:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, data):
        self.size += 1
        if self.root is None:
            self.root = Node(data)

        else:
            curr = self.root
            while(curr.next):
                curr = curr.next
            curr.next = Node(data)

    def insertAtHead(self, data):
        temp = self.root
        self.root = Node(data, temp)
        self.size += 1

    def __str__(self):
        dataString = []
        current = self.root
        while (current):
            dataString.append(str(current.data))
            current = current.next
        return ' -> '.join(dataString)

    def __eq__(self, other):
        thisNode = self.root
        otherNode = other.root

        while (thisNode and otherNode):
            if thisNode.data != otherNode.data:
                return False
            thisNode, otherNode = thisNode.next, otherNode.next
        return thisNode == otherNode

    def __len__(self):
        return self.size

class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
