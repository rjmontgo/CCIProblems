from lib.linkedlist import *

def findCycleStart(l1):
    if l1.root is None:
        return None
    # Determine if there is a cycle by
    # setting a slow mover and a fast mover
    slow = l1.root
    fast = l1.root.next
    if fast.next is None:
        return None
    fast = fast.next
    while slow and fast and slow is not fast:
        slow = slow.next
        fast = fast.next
        if fast.next is None:
            return None
        fast = fast.next

    # if there is no cycle return None
    if fast is None:
        return None

    # These will meet x steps before the start of the cycle where
    # x is the length of the chain before the cycle
    fast = l1.root

    # reset one of the movers to the chain and move both 1 step at a time
    # and return when they are equal
    while fast is not slow:
        fast = fast.next
        slow = slow.next
    return fast
