from queue import Queue
from tree_node import create_tree

def levelorder_search(root, value):
    if not root:
        return

    else:
        IS_FOUND = False
        q = Queue()
        q.put(root)

        while not q.empty():
            root = q.get()

            if root.val == value:
                IS_FOUND = True
                break

            if root.left:
                q.put(root.left)

            if root.right:
                q.put(root.right)

        return IS_FOUND

print(levelorder_search(create_tree(), 5))
