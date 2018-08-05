from lib.linkedlist import LinkedList
import math

def addLists(l1, l2):
    # Find the length of both lists
    curr1, len1 = l1.root, 0
    curr2, len2 = l2.root, 0
    while (curr1 or curr2):
        if curr1:
            len1 += 1
            curr1 = curr1.next
        if curr2:
            len2 += 1
            curr2 = curr2.next
    # assign them to long/short respectively
    long, longlen, short, shortlen = (l1, len1, l2, len2) if len1 > len2 else \
                                        (l2, len2, l1, len1)
    # call AddListsHelper to do this in one pass
    rem = addListsHelper(long.root, short.root, longlen - shortlen)

    # get the remainder of AddListsHelper and if != 0 then insert at front
    if rem > 0:
        long.insertAtHead(rem)
    # return long
    return long

def addListsHelper(long, short, stop):
    if not long:
        return 0
    if stop > 0:
        sum = long.data + addListsHelper(long.next, short, stop - 1)
        long.data = sum % 10
        return math.floor(sum / 10)
    else:
        sum = long.data + short.data + addListsHelper(long.next, short.next, stop)
        long.data = sum % 10
        return math.floor(sum / 10)
