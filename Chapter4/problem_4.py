def checkBalanced(binaryTree):
    return recurisBalanced(binaryTree.root)[1]

def recurisBalanced(node):
    if not node:
        return (0, True)
    if not node.left and not node.right:
        return (1, True)
    lisBalanced = recurisBalanced(node.left)
    risBalanced = recurisBalanced(node.right)
    if lisBalanced[1] and risBalanced[1]:
        return (max(lisBalanced[0], risBalanced[0]) + 1,
                    abs(lisBalanced[0] - risBalanced[0]) <= 1)
    return (max(lisBalanced[0], risBalanced[0]) + 1, False)
