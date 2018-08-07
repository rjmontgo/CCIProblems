from lib.graph import *

from problem_1 import isRoute

def test_nodes_next_to_each_other():
    nodeLeft = Node()
    nodeRight = Node()

    nodeLeft.children.append(nodeRight)
    nodeRight.children.append(nodeLeft)

    assert True == isRoute(nodeLeft, nodeRight)

def test_one_node_off():
    nodeLeft = Node()
    nodeMid = Node()
    nodeRight = Node()

    nodeLeft.children.append(nodeMid)
    nodeMid.children.append(nodeRight)
    nodeMid.children.append(nodeLeft)
    nodeRight.children.append(nodeMid)

    assert True == isRoute(nodeLeft, nodeRight)


def test_not_in_same_graphs():

    nodeLeft = Node()
    for i in range(5):
        nodeLeft.children.append(Node())

    nodeRight = Node()
    for i in range(5):
        nodeRight.children.append(Node())

    assert False == isRoute(nodeLeft, nodeRight)


def test_nine_node_graph():
# Graph looks like this: x denotes node to search from.

#             5
#             |
# 1 - x - 2 - 4 - x - 7
#         |   |
#         3   6

    node1 = Node()
    routeNode1 = Node()
    node2 = Node()
    node3 = Node()
    node4 = Node()
    node5 = Node()
    routeNode2 = Node()
    node6 = Node()
    node7 = Node()

    node1.children.append(routeNode1)
    routeNode1.children.append(node1)
    routeNode1.children.append(node2)
    node2.children.append(routeNode1)
    node2.children.append(node3)
    node2.children.append(node4)
    node3.children.append(node2)
    node4.children.append(node2)
    node4.children.append(node6)
    node4.children.append(node5)
    node4.children.append(routeNode2)
    node5.children.append(node4)
    node6.children.append(node4)
    routeNode2.children.append(node4)
    routeNode2.children.append(node7)
    node7.children.append(routeNode2)
