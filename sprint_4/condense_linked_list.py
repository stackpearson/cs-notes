def condense_linked_list(node):
    # need to traverse LL & keep track of each node in a list
    # as we iterate, check our list to see if the current node in the LL exists in our list
        # if it does, we need to remove that value from the LL
        
    previous = node
    current = previous.next
    keys = [previous.value]
    
    while current:
        currentVal = current.value
        # print('keys', keys)
        
        if currentVal in keys:
            previous.next = current.next
            current = current.next
        else:
            keys.append(currentVal)
            previous = current
            current = previous.next
        
    return node

    # print(node.next.value)