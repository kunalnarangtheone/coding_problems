from bst_create import create_bst
from bst_traverse import traverse_bst
from bst_search import search_bst
from tree_node import TreeNode


def insert_bst(root, value):
    if not root:
        return TreeNode(value)
    
    if value < root.val:
        root.left = insert_bst(root.left, value)

    else:
        root.right = insert_bst(root.right, value)

    return root

root = create_bst()
insert_bst(root, 7)
search_bst(root, 7)
