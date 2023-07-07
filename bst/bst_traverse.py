# from bst_create import create_bst

def traverse_bst(root):
    if not root:
        return

    else:
        print(root.val)

        if root.left:
            traverse_bst(root.left)

        if root.right:
            traverse_bst(root.right)

# traverse_bst(create_bst())
