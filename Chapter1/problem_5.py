
def isOneAway(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    if (abs(len1 - len2) > 1):
        return False

    large, small = (str1, str2) if len1 > len2 else (str2, str1)
    i, len1 = 0, len(large)
    j, len2 = 0, len(small)
    foundDifference = False
    while (i < len1 and j < len2):
        if large[i] != small[i]:
            if foundDifference:
                return False
            foundDifference = True
            if len1 == len2:
                i += 1
        else:
            i += 1
        j += 1

    return True
