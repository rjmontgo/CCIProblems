def sortStack(unsortedStack):
    tempStack = []
    while unsortedStack:
        comp = unsortedStack.pop()
        numPop = len(unsortedStack)
        while unsortedStack:
            val = unsortedStack.pop()
            if val < comp:
                temp = val
                val = comp
                comp = temp
            tempStack.append(val)

        while numPop > 0:
            unsortedStack.append(tempStack.pop())
            numPop -= 1
        tempStack.append(comp)
    while tempStack:
        unsortedStack.append(tempStack.pop())
    return unsortedStack
