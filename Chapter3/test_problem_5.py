from problem_5 import sortStack

def test_simple_stack():
    unsortedStack = [1, 5, 4, 6, 3]
    sortedStack = [6, 5, 4, 3, 1]

    newSortedStack = sortStack(unsortedStack)

    assert newSortedStack == sortedStack

def test_sorted_stack():
    unsortedStack = [6, 5, 4, 3, 1]
    sortedStack = [6, 5, 4, 3, 1]

    newSortedStack = sortStack(unsortedStack)

    assert newSortedStack == sortedStack
