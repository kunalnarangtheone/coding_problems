from bst_create import create_bst
from queue import Queue

def height_bst(root):
    if not root:
        return 0

    else:
        q = Queue()
        q.put(root)
        height = 0

        while True:
            node_count = q.qsize()
            if node_count == 0:
                break

            while node_count > 0:
                node = q.get()

                if node.left:
                    q.put(node.left)

                if node.right:
                    q.put(node.right)

                node_count -=1

            height+=1

        return height


print(height_bst(create_bst()))
