from construct_bst_from_list import bst_from_list

def inorder_traversal(root):
    nodes = []
    def inorder(node):
        if not node:
            return

        if node.left:
            inorder(node.left)

        nodes.append(node.val)

        if node.right:
            inorder(node.right)

    inorder(root)
    return nodes

root = bst_from_list([2, 1, 4, 7, 6, 5, 0])
print(inorder_traversal(root))


