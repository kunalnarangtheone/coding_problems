from bst_create import create_bst

def inorder(root_node):
    """Does left -> root -> right"""
    if not root_node:
        return

    else:
        inorder(root_node.left)
        print(root_node.val, end = " -> ")
        inorder(root_node.right)

inorder(create_bst())
