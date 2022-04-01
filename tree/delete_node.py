from tree_node import create_tree
from queue import Queue
from levelorder_traversal import levelorder

def deepest_node(root):
    """Finds the deepest node from a tree"""
    if not root:
        return

    else:
        q = Queue()
        q.put(root)

        while not q.empty():
            node = q.get()

            if node.left:
                q.put(node.left)

            if node.right:
                q.put(node.right)

        return node.val

def delete_deepest_node(root, deepest):
    """Deletes the deepest node from a tree"""
    if not root:
        return

    else:
        q = Queue()
        q.put(root)

        while not q.empty():
            node = q.get()

            if node.val == deepest:
                node = None
                break

            if node.right.val == deepest:
                node.right = None
                break

            if node.left.val == deepest:
                node.left = None
                break

            if node.left:
                    q.put(node.left)

            if node.right:
                    q.put(node.right)

        return root


def delete_node(root, value, deepest):
    if not root:
        return None

    else:
        q = Queue()
        q.put(root)

        while q.empty():
            node = q.get()

            if node.val == value:
                deep = deepest_node(root)
                node.val = deep
                delete_deepest_node(root, deep)

            if node.left:
                q.put(node.left)

            if node.right:
                q.put(node.right)

        return root


tree = create_tree()
deepest = deepest_node(tree)
levelorder(delete_node(tree, 3, deepest))
