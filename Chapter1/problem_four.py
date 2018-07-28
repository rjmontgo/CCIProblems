def isPalinPerm(str):
    if len(str) <= 2:
        return True
    isOdd = False
    if len(str) % 2 != 0:
        isOdd = True
    dic = {}
    for elem in str:
        dic[elem] = dic.get(elem, 0) + 1
    isFound = False
    for value in dic.values():
        if (value % 2 != 0 and isOdd and not isFound):
            isFound = True
        elif(value % 2 != 0):
            return False

    return True
