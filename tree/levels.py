from collections import deque
from levelorder_traversal import levelorder

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.level = None


def create_bst():
    root = TreeNode(5)
    node1 = TreeNode(2)
    node2 = TreeNode(8)
    node3 = TreeNode(1)
    node4 = TreeNode(3)
    node5 = TreeNode(6)
    node6 = TreeNode(10)
    node7 = TreeNode(7)

    root.left = node1
    root.right = node2

    node1.left = node3
    node1.right = node4

    node2.left = node5
    node2.right = node6

    node5.right = node7

    return root

def get_levels(root):
    if not root:
        return None

    else:
        root.level = 1
        q = deque()
        q.append(root)

        while True:
            node_count = len(q)

            if node_count == 0:
                break

            while node_count > 0:
                node = q.pop()

                if node.left:
                    node.left.level = node.level + 1
                    q.append(node.left)

                if node.right:
                    node.right.level = node.level + 1
                    q.append(node.right)

                node_count-=1

root = create_bst()
get_levels(root)
levelorder(root) # change printing val to level in levelorder for printing results
