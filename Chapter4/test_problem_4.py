from lib.binarytree import *
from problem_4 import checkBalanced

"""
 o
"""
def test_one_node():
    binaryTree = BinaryTree()
    binaryTree.root = Node(data = 1)

    assert checkBalanced(binaryTree)

"""
  o
 /  \
o    o
"""
def test_three_nodes():
    binaryTree = BinaryTree()
    binaryTree.root = Node(Node(data=1), Node(data=3), 2)

    assert checkBalanced(binaryTree)

"""
      o
     / \
    o   o
   /
  o
 /
o
"""
def test_five_nodes():
    binaryTree = BinaryTree()
    binaryTree.root = Node(Node(
                            left=Node(
                            left=Node(data=-1), data=0),data=1),
                            Node(data=3), 2)

    assert not checkBalanced(binaryTree)

"""
        o
       / \
      o   o
       \   \
        o   o
         \
          o
"""
def test_six_nodes():
    binaryTree = BinaryTree()
    binaryTree.root = Node(Node(right=Node(right=Node())), Node(right=Node()))


    assert not checkBalanced(binaryTree)

"""
      o
     / \
    o   o
   /     \
  o       o
   \
    o
     \
      o
"""

def test_seven_nodes():
    binaryTree = BinaryTree()
    binaryTree.root = Node(Node(left=Node(right=Node(right=Node()))),
                           Node(right=Node()))

    assert not checkBalanced(binaryTree)
