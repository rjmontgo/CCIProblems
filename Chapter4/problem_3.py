from lib.linkedlist import LinkedList
from lib.binarytree import *

def getDepthLists(binTree):
    arr = []
    recurDepthLists(binTree.root, 0, arr)
    return arr

def recurDepthLists(node, depth, arr):
    if not node:
        return
    if depth >= len(arr):
        arr.append(LinkedList())
    arr[depth].add(node.data)
    recurDepthLists(node.left, depth + 1, arr)
    recurDepthLists(node.right, depth + 1, arr)
