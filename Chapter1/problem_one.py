def isUnique(uniquestring):
    # Sort
    ls = list(uniquestring)
    ls.sort()

    # loop checking each index with successor
    for i in range(len(ls) - 1):
        if ls[i] == ls[i + 1]:
            return False

    return True
