def isPermutation(s1, s2):
    if len(s1) != len(s2):
        return False

    if sorted(s1) == sorted(s2):
        return True
    return False
