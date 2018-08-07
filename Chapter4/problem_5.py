import math

def validateBST(binTree):
    return validationHelper(binTree.root, -math.inf, math.inf)

def validationHelper(node, low, high):
    if not node:
        return True
    if node.data <= low or node.data > high:
        return False
    validLeft = validationHelper(node.left, low, node.data)
    validRight = validationHelper(node.right, node.data, high)
    return validLeft and validRight
