import lib.linkedlist
import math


def isPalindrome(paliList, length, testId):
    if length <= 1:
        return True
    mid = math.floor(length / 2)
    curr = paliList.root
    index, paliStack = 0, []
    while curr and index < mid:
        paliStack.append(curr.data)
        curr = curr.next
        index += 1
    curr = curr if length % 2 is 0 else curr.next
    while curr:
        if paliStack.pop() != curr.data:
            return False
        curr = curr.next
    return len(paliStack) == 0
