from bst_create import create_bst

def preorder(root_node):
    """Does root -> left -> right"""
    if not root_node:
        return

    else:
        print(root_node.val, end = " -> ")
        preorder(root_node.left)
        preorder(root_node.right)


preorder(create_bst())
