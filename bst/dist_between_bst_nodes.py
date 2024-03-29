# from bst_traverse import traverse_bst
from treenode import TreeNode
from lca import find_lca
from depth import find_depth
from construct_bst_from_list import bst_from_list

def dist_bw_nodes():
    p = TreeNode(5)
    q = TreeNode(0)

    root = bst_from_list([2, 1, 4, 7, 6, 5, 0])
    p_depth = find_depth(root, p.val, 1)
    q_depth = find_depth(root, q.val, 1)

    if not p_depth or not q_depth:
        return -1

    lca_depth = find_depth(root, find_lca(root, p, q), 1)
    return p_depth + q_depth - (2 * lca_depth)

print(dist_bw_nodes())

