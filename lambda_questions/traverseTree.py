def traverseTree(t):
    if t is None:
        return []

    result = []
    queue = []
    queue.append(t)

    while len(queue) != 0:
        node = queue.pop(0)
        result.append(node.value)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

    return result