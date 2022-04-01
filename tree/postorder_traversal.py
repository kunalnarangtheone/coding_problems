from tree_node import create_tree

def postorder(root_node):
    """Does left -> right -> root"""
    if not root_node:
        return

    else:
        postorder(root_node.left)
        postorder(root_node.right)
        print(root_node.val, end = " -> ")

postorder(create_tree())
