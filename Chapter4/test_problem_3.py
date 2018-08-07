from problem_3 import getDepthLists
from lib.linkedlist import LinkedList
from lib.binarytree import *

def test_one_node():
    binaryTree = BinaryTree()
    binaryTree.root = Node(data=1)
    arrlinkedResult = [LinkedList()]
    arrlinkedResult[0].add(1)

    assert arrlinkedResult == getDepthLists(binaryTree)

def test_three_nodes():
    binaryTree = BinaryTree()
    binaryTree.root = Node(Node(data=1), Node(data=3), 2)
    arrlinkedResult = [LinkedList(), LinkedList()]
    arrlinkedResult[0].add(2)
    arrlinkedResult[1].add(1)
    arrlinkedResult[1].add(3)

    assert arrlinkedResult == getDepthLists(binaryTree)


def test_five_nodes():
    binaryTree = BinaryTree()
    binaryTree.root = Node(Node(left=Node(data=1), data=2),
                           Node(right=Node(data=5), data=4), 3)
    arrlinkedResult = [LinkedList(), LinkedList(), LinkedList()]
    arrlinkedResult[0].add(3)
    arrlinkedResult[1].add(2)
    arrlinkedResult[1].add(4)
    arrlinkedResult[2].add(1)
    arrlinkedResult[2].add(5)

    assert arrlinkedResult == getDepthLists(binaryTree)


def test_seven_nodes():
    binaryTree = BinaryTree()
    binaryTree.root = Node(Node(Node(data=1), Node(data=3), 2),
                           Node(Node(data=5), Node(data=7), 6), 4)

    arrlinkedResult = [LinkedList(), LinkedList(), LinkedList()]
    arrlinkedResult[0].add(4)
    arrlinkedResult[1].add(2)
    arrlinkedResult[1].add(6)
    arrlinkedResult[2].add(1)
    arrlinkedResult[2].add(3)
    arrlinkedResult[2].add(5)
    arrlinkedResult[2].add(7)

    assert arrlinkedResult == getDepthLists(binaryTree)
