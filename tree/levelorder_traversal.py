from queue import Queue
from tree_node import create_tree

def levelorder(root):
    if not root:
        return

    else:
        q = Queue()
        q.put(root)

        while not q.empty():
            root =  q.get()
            print(root.val)

            if root.left:
                q.put(root.left)

            if root.right:
                q.put(root.right)


def levelorder_2(root):
    if not root:
        return

    else:
        q = Queue()
        q.put(root)
        traverse = []

        while True:
            node_count = q.qsize()
            if node_count == 0:
                break

            while node_count > 0:
                node = q.get()
                traverse.append(node.val)

                if node.left:
                    q.put(node.left)

                if node.right:
                    q.put(node.right)

                node_count-=1

        return traverse
