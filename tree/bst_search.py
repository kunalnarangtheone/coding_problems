from bst_create import create_bst

def search_bst(root, value):
    if not root:
        return

    else:
        if value == root.val:
            print("Value has been found!")
            return

        elif value < root.val:
            search_bst(root.left, value)

        else:
            search_bst(root.right, value)
