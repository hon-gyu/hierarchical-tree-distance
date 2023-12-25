import numpy as np
from anytree import Walker

def edge_weight(edge, tau=3):
    """weight of edge (pa, ch)"""
    pa = edge[0]
    ch = edge[1]
    if pa.is_root:
        return 1 / (np.log10(len(ch.children)) + 1)
    else:
        parent_edge = (pa.parent, pa)
        numerator = edge_weight(parent_edge)
        denominator = 3 * np.log10(len(pa.children)) + 1
        return numerator / denominator

def AKB_distance(node1, node2):
    """AKB distance between two nodes"""
    path = Walker().walk(node1, node2)
    path_left = list(path[0])
    path_left.append(path[1])
    path_right = [path[1]]
    path_right += list(path[2])
    path_right
    edges_left = [(node1_, node2_) for node1_, node2_ in zip(path_left[::-1][:-1], path_left[::-1][1:])]
    edges_right = [(node1_, node2_) for node1_, node2_ in zip(path_right[:-1], path_right[1:])]
    dist = sum([edge_weight(edge) for edge in edges_left]) + sum([edge_weight(edge) for edge in edges_right])
    return dist