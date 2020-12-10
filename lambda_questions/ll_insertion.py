# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def insertValueIntoSortedLinkedList(l, value):
    nodeToInsert = ListNode(value)
    
    #  if list is empty, return our nodeToInsert
    if l is None:
        l = nodeToInsert
        return l
        
    current = l
    
    # single node in LL: head > value -> have nodeToInsert point to head
    if current.value > value:
        nodeToInsert.next = current
        return nodeToInsert
    
    # while current is true  
    while current:
        # print(current.value)
        # single Node in LL: head < value have head point to nodeToInsert
        if current.next is None:
            current.next = nodeToInsert
            return l
        
        # handling our insertion
        # if current is less than next and next is more than the value, we know that's where we want to stick our nodeToInsert
        elif current.value < value and current.next.value > value:
            nodeToInsert.next = current.next
            current.next = nodeToInsert
            return l
        
        #  this is how we're traversing the list, if none of the above reqs are met, me move to the next node   
        else:
            current = current.next
