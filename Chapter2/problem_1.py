from lib.linkedlist import LinkedList

# 2.1
# Write code to remove duplicates from a LinkedList

def removeDups(linkedList):
    # Check if list is empty
    if linkedList.root is None:
        return linkedlist

    # initialize foundData with setData
    foundData = { linkedList.root.data }
    # set current pointer and previous pointer for removal
    current = linkedList.root.next
    previous = linkedList.root
    # While the current node is not None
    while(current):
        # if the data in the current element is in the set
        if current.data in foundData:
            # Remove the element
            ## set previous element's .next to the current element's .next
            prev.next = current.next
        else:
            # Add the current data in the element to the set
            foundData.add(current.data)
            prev = current


        # update the pointers
        current = current.next

    # we have reached the end and can return the list
    return linkedList






# Parameters (LinkedList: linkedList)
# Return -> linkedList with no duplicates


# Simplest Problem
# IN - 1
# OUT - 1

# V2
# IN - 1 -> 2 -> 2
# OUT - 1 -> 2

# V3
# IN - 1 -> 3 -> 2 -> 3
# OUT - 1 -> 3 -> 2

# V4
# IN - 1 -> 2 -> 3 -> 2 -> 1 -> 3
# OUT - 1 -> 2 -> 3

# Edge Cases
# Empty list -> return LinkedList head

# Patterns / Notes
# Sorting would put duplicates next to each other
#  - Very difficult and time consuming
# Maintaining a set of previous values could accomplish this
#  - O(n^2) run time to loop through list and add to set

# Solutions / complexity
# 1. Sort the list and duplicates will be next to each other
#   / O(n^2) Time - with in-place merge sort because of the way the
#   /               list is structured
#   / O(1) Space - no extra space
#   / O(nlog(n)) Time - if you copy everything to an array and merge sort that
#   / O(n) Space - to hold the array

# 2. Use a set to hold the values that you have found
#   / O(n^2) Time - to loop through list and add items to the set
#   / O(n) Space - to hold the set in the case where every item in the list
#                  must be stored.

# 3. Use a hashtable to lookup if we have found the value
#   / O(n^2) Time - This is better stated as O(n) since the average case lookup
#                   time for a hash table is O(1).
#   / O(n) Space - to hold the hash table, which python dictionaries are
#                  implemented as hash tables.

# It turns out that sets in python use a hashtable as its underlying
# datastructure so solution 2 will actually be O(n) in the average case.
