def csBinaryTreeInvert(root):
    if root:
        root.left, root.right = csBinaryTreeInvert(root.right), csBinaryTreeInvert(root.left)
        return root