def reverseLinkedList(head):
	prevPointer, midPointer = None, head
	
	while midPointer is not None:
		nextPointer = midPointer.next
		midPointer.next = prevPointer
		prevPointer = midPointer
		midPointer = nextPointer
	return prevPointer