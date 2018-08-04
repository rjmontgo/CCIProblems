def deleteMiddle(node):
    # Thought the parameters of the problem were that I would not have to deal
    # with the node passed in being the last node so I will handle this case here
    if not node.next:
        return

    # Otherwise you can just copy the next node data into the current node
    # Then move the next pointer to the next.next node
    node.data = node.next.data
    node.next = node.next.next
