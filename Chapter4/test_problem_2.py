from lib.binarytree import *
from problem_2 import buildTree

def test_build_one_node_tree():
    arr = [1]
    binaryTree = BinaryTree()
    binaryTree.root = Node(data=1)
    assert binaryTree == buildTree(arr)

def test_build_two_node_tree():
    arr = [1, 2, 3]
    binaryTree = BinaryTree()
    binaryTree.root = Node(Node(data=1), Node(data=3), 2)
    assert binaryTree == buildTree(arr)

def test_build_seven_node_tree():
    arr = [1, 2, 3, 4, 5, 6, 7]
    binaryTree = BinaryTree()
    binaryTree.root = Node(Node(Node(data=1), Node(data=3), 2), \
                           Node(Node(data=5), Node(data=7), 6), 4)

    assert binaryTree == buildTree(arr)
