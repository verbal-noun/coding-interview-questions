def invertTree(root): 
    if root is None: 
        return None 

    left = invertTree(root.left)
    right = invertTree(root.right)
    root.left = right
    root.right = left 

    return root 