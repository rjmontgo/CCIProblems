from collections import deque

def isRoute(node1, node2):
    q1 = deque()
    q2 = deque()
    s1 = set()
    s2 = set()
    s1.add(node1)
    s2.add(node2)
    q1.append(node1)
    q2.append(node2)
    while q1 and q2:
        found1 = q1.popleft()
        found2 = q2.popleft()
        if found1 in s2 or found2 in s1:
            return True

        for child in found1.children:
            if not child in s1:
                s1.add(child)
                q1.append(child)

        for child in found2.children:
            if not child in s2:
                s2.add(child)
                q2.append(child)
    return False
