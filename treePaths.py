def treePaths(t):
    res = []
    
    # base case - empty tree
    if t is None:
        return res
        
     # pre order would work best   
    if t.left is None and t.right is None:
        s = f'{t.value}'
        res.append(s)
        return res
        
    string = ''
    recurse(t, string, res)
    return res

# need to call over tree recursively   
def recurse(root, s, res):
    
    # if we just have a head append the value
    if root.left is None and root.right is None:
        res.append(s + f'{root.value}')
        
    
    # go over left hand side until we hit null
    s += f'{root.value}->'    
    if root.left is not None:
        recurse(root.left, s, res)
        
    #  go over right unitil we hit null   
    if root.right is not None:
        recurse(root.right, s, res)