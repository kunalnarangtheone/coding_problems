from treenode import TreeNode

def bst_from_list(li):
    def add_node(node, val):
        if not node:
            return TreeNode(val)

        if val < node.val:
            node.left = add_node(node.left, val)

        else:
            node.right = add_node(node.right, val)

        return node
    
    root = TreeNode(li[0])
    
    for val in li[1:]:
        add_node(root, val)

    return root

