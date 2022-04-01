from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.hd = None

def top_view(root):
    """Find the nodes that can be viewed from the root node. We are going to do level order + vertical order traversal."""
    if not root:
        return

    else:
        hd = dict()
        q = deque()
        root.hd = 0
        q.append(root)

        while q:
            node = q.popleft()

            if node.hd not in hd:
                hd[node.hd] = [node.val]
            else:
                hd[node.hd].append(node.val)

            if node.left:
                node.left.hd = node.hd - 1
                q.append(node.left)

            if node.right:
                node.right.hd = node.hd + 1
                q.append(node.right)

        traverse = [str(values[0]) for values in hd.values()]
        return " ".join(traverse)

def create_tree():
    root = Node(5)
    node1 = Node(2)
    node2 = Node(8)
    node3 = Node(1)
    node4 = Node(3)
    node5 = Node(6)
    node6 = Node(10)

    root.left = node1
    root.right = node2

    node1.left = node3
    node1.right = node4

    node2.left = node5
    node2.right = node6

    return root

print(top_view(create_tree()))
