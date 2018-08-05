from lib.linkedlist import LinkedList

def partitionList(list, val):
    lowerList = LinkedList()
    upperList = LinkedList()
    current = list.root
    while current:
        if current.data < val:
            lowerList.insertAtHead(current.data)
        else:
            upperList.insertAtHead(current.data)
        current = current.next

    if lowerList.root:
        current = lowerList.root
        while (current.next):
            current = current.next
        current.next = upperList.root
        return lowerList
    else:
        return upperList
