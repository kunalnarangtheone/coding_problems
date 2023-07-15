from treenode import TreeNode
from inorder import inorder_traversal
from construct_bst_from_list import bst_from_list

def balance_bst(nodes, l, r):
    if l > r:
        return None
    
    mid = (l + r) // 2
    node = TreeNode(nodes[mid])
    node.left = balance_bst(nodes, l, mid - 1)
    node.right = balance_bst(nodes, mid + 1, r)
    return node

root = bst_from_list([2, 1, 4, 7, 6, 5, 0])
nodes = inorder_traversal(root)

new_node = balance_bst(nodes, 0, len(nodes) - 1)
print(inorder_traversal(new_node))