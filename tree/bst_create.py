from tree_node import TreeNode

def create_bst():
    root = TreeNode(5)
    node1 = TreeNode(2)
    node2 = TreeNode(8)
    node3 = TreeNode(1)
    node4 = TreeNode(3)
    node5 = TreeNode(6)
    node6 = TreeNode(10)
    # node7 = TreeNode(7)

    root.left = node1
    root.right = node2

    node1.left = node3
    node1.right = node4

    node2.left = node5
    node2.right = node6

    # node5.right = node7

    return root
