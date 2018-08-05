def linkIntersection(l1, l2):
    curr1 = l1.root
    curr2 = l2.root
    len1 = 0
    len2 = 0
    while curr1 or curr2:
        if curr1 == curr2:
            return curr1
        if curr1:
            curr1 = curr1.next
            len1 += 1
        if curr2:
            curr2 = curr2.next
            len2 += 1

    long, short, diff = (l1, l2, len1 - len2) if len1 > len2 else \
                            (l2, l1, len2 - len1)
    longcurr = long.root
    shortcurr = short.root
    while diff > 0:
        longcurr = longcurr.next
        diff -= 1

    while longcurr and shortcurr:
        if longcurr == shortcurr:
            return longcurr
        shortcurr = shortcurr.next
        longcurr = longcurr.next
    return None
