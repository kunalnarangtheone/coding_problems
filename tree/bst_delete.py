from bst_create import create_bst

def find_successor(node):
    if not node:
        return "Cannot find successor for an empty node"

    if not node.right:
        return None

    else:
        node = node.right

        if node.left:
            find_successor(node)


def delete_bst(root, value):
    if not root:
        return "BST is empty! Cannot delete from an empty tree!"

    else:
        #1 When node to be deleted has no childen, i.e. leaf node
        if value == root.value:
            return # Handle this case

        if value < root.value:
            if root.left:
                delete_bst(root.left, value)

            if root.right:
                delete_bst(root.right, value)

        if value > root.value:
            if root.right





        #2 When node to be deleted has one child only (either left or right)

        #3 When node to be deleted has two childen (in this case, we need to find successor and apply either 1 or 2)
