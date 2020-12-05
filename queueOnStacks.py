def queueOnStacks(requests):
    left = Stack()
    right = Stack()

    def insert(x):
        while not left:
            right.push(left.pop())
        left.push(x)
        while not right:
            left.push(right.pop())

    def remove():
        return left.pop()