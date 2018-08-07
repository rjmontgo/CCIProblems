import math

def findSuccessor(node):
    if node.right:
        return findHelper(node.right, -math.inf)
    elif node.parent.data > node.data:
        return node.parent
    else:
        return None

def findHelper(node, val):
    if node.data > val:
        if node.left:
            return findHelper(node.left, val)
        else:
            return node
    else:
        raise ValueError('can\'t be less that negative infinity')
