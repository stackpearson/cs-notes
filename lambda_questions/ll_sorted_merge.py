# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

#  here is a really great walk through of this problem as well https://www.youtube.com/watch?v=r3MAkVZkD0s

def mergeTwoLinkedLists(l1, l2):
    # create a new list to add our values to
    head = ListNode(0)
    ptr = head
    
    while True:
        if l1 is None and l2 is None:
            break
        elif l1 is None:
            ptr.next = l2
            break
        elif l2 is None:
            ptr.next = l1
            break
        else:
            smallerValue = 0
            if l1.value < l2.value:
                smallerValue = l1.value
                l1 = l1.next
            else:
                smallerValue = l2.value
                l2 = l2.next
            newNode = ListNode(smallerValue)
            ptr.next = newNode
            ptr = ptr.next
    return head.next