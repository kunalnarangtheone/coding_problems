from bst_create import create_bst

def traverse_bst(root):
    if not root:
        return

    else:
        print(root.val)

        if root.left:
            bst_traverse(root.left)

        if root.right:
            bst_traverse(root.right)
