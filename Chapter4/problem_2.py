import math
from lib.binarytree import *

def buildTree(arr):
    binaryTree = BinaryTree()
    binaryTree.root = searchHelper(arr, 0, len(arr) - 1)
    return binaryTree

def searchHelper(arr, low, high):
    if low > high:
        return None
    mid = math.floor( (high - low) / 2 ) + low
    node = Node(data=arr[mid])
    node.left = searchHelper(arr, low, mid - 1)
    node.right = searchHelper(arr, mid + 1, high)
    return node
