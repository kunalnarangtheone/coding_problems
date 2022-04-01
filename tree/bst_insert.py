from bst_create import create_bst
from bst_traverse import traverse_bst
from bst_search import search_bst
from tree_node import TreeNode


def insert_bst(root, value):
    if not root:
        return TreeNode(value)

    else:
        if value == root.val:
            return

        elif value < root.val:
            if root.left:
                insert_bst(root.left, value)
            else:
                root.left = TreeNode(value)

        else:
            if root.right:
                insert_bst(root.right, value)
            else:
                root.right = TreeNode(value)

        return "The node has been successfully inserted"

root = create_bst()
insert_bst(root, 7)
search_bst(root, 7)
