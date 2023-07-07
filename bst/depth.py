def find_depth(node, val, depth):
    if node == None:
        return -1

    if val == node.val:
        return depth
    
    if val < node.val:
        return find_depth(node.left, val, depth + 1)
    
    else:
        return find_depth(node.right, val, depth + 1)