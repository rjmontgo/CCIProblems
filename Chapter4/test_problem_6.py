from lib.binarytree import *
from problem_6 import findSuccessor

"""
   3
  /
 2
"""
def test_two_node():
    binaryTree = BinaryTree()
    binaryTree.root = Node(left=Node(data=2), data=3)
    binaryTree.root.left.parent = binaryTree.root
    assert findSuccessor(binaryTree.root.left) is binaryTree.root

"""
   3
  /
 2
  \
   1
"""
def test_three_node():
    binaryTree = BinaryTree()
    binaryTree.root = Node(left=Node(right=Node(data=1), data=2), data=3)

    assert findSuccessor(binaryTree.root.left) is binaryTree.root.left.right

"""
    5
     \
      7
     / \
    6   12
        /
       8
"""
def test_five_node():
    binaryTree = BinaryTree()
    binaryTree.root = Node(right=Node(Node(data=6),
                      Node(left=Node(data=8), data=12), data=7))

    assert findSuccessor(binaryTree.root.right) is \
                        binaryTree.root.right.right.left
