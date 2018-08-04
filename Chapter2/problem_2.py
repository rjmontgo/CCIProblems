from lib.linkedlist import LinkedList

def kFromEnd(list, k):
    if not list.root:
        return None

    current = list.root
    kNode = None
    while (current.next):
        if kNode:
            kNode = kNode.next
        elif k > 0:
            k -= 1
        if k is 0 and not kNode:
            kNode = list.root
        current = current.next
    if k is 0 and not kNode:
        kNode = list.root
    return kNode.data
