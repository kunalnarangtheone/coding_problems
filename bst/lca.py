def find_lca(node, p, q):
    if p.val > q.val:
        greater, smaller = p.val, q.val

    else:
        greater, smaller = q.val, p.val

    def lca(node, greater, smaller):
        if node:
            if node.val >= smaller and node.val <= greater:
                return node.val
            
            elif node.left and smaller <= node.val and greater <= node.val:
                return lca(node.left, greater, smaller)
            
            elif node.right and smaller > node.val and greater > node.val:
                return lca(node.right, greater, smaller)
            

    return lca(node, greater, smaller)
            
