def csBSTRangeSum(root, lower, upper):
    values = []
    helper(root, values, lower, upper)

    return sum(values)
    
def helper(root, values, lower, upper):
    if root is None:
        return
    else:
        helper(root.left, values, lower, upper)
        helper(root.right, values, lower, upper)
        if (root.value >= lower) and (root.value <= upper):
            values.append(root.value)

