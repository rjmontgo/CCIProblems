class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def __hash__(self):
        return hash(self.obj)

    def __eq__(self, other):
        if not isinstance(other, BinaryTree):
            return NotImplemented
        return self.equalHelper(self.root, other.root)

    def equalHelper(self, thisNode, otherNode):
        if thisNode is None or otherNode is None:
            return thisNode is otherNode
        if thisNode.data != otherNode.data:
            return False
        return self.equalHelper(thisNode.left, otherNode.left) and \
                self.equalHelper(thisNode.right, otherNode.right)

class Node:

    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
