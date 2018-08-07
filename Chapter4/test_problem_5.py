from lib.binarytree import *
from problem_5 import validateBST

"""
    3
   / \
  2   4
"""
def test_three_node():
    binTree = BinaryTree()
    binTree.root = Node(Node(data=2), Node(data=4), 3)

    assert validateBST(binTree)

"""
      4
    /   \
   2     5
    \
     3
"""
def test_five_node():
    binTree = BinaryTree()
    binTree.root = Node(Node(right=Node(data=3), data=2), Node(data=5), 4)

    assert validateBST(binTree)


"""
      5
     / \
    5   6
   /     \
  2       7
   \
    3
"""
def test_six_node():
    binTree = BinaryTree()
    binTree.root = Node(Node(left=Node(right=Node(data=3), data=2), data=5),
                        Node(right=Node(data=7), data=6), 5)

    assert validateBST(binTree)


"""
    5
     \
      3

"""
def test_invalid_BST():
    print("Test")
    binTree = BinaryTree()
    binTree.root = Node(right=Node(data=3), data=5)

    assert not validateBST(binTree)

"""
     5
   /   \
  4     7
   \
    6

"""
def test_long_invalid_BST():
    binTree = BinaryTree()
    binTree.root = Node(Node(right=Node(data=6), data=4), Node(data=7), 5)

    assert not validateBST(binTree)
