from tree_node import TreeNode
from queue import Queue
from levelorder_traversal import levelorder

def create_tree_for_insertion():
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(4)
    node4 = TreeNode(5)
    node5 = TreeNode(6)
    node6 = TreeNode(7)
    node7 = TreeNode(8)
    node8 = TreeNode(9)

    root.left = node1
    root.right = node2

    node1.left = node3
    node1.right = node4

    node2.left = node5
    node2.right = node6

    node3.left = node7
    node3.right = node8

    return root

def insert_node_using_levelorder(root, value):
    ins = TreeNode(value)

    if not root:
        return ins

    else:
        q = Queue()
        q.put(root)

        while not q.empty():
            node = q.get()

            if node.left:
                q.put(node.left)
            else:
                node.left = ins
                break

            if node.right:
                q.put(node.right)
            else:
                node.right = ins
                break

        return root


levelorder(insert_node_using_levelorder(create_tree_for_insertion(), 20))
