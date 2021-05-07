
def find_successor(tree, target):
    tree_nodes = in_order_traversal(tree, [])

    for idx, node in enumerate(tree_nodes):
        if node != target:
            continue

        if idx == (tree_nodes) - 1:
            return None
        return tree_nodes[idx+1]


def in_order_traversal(node, array):

    if node is None:
        return array

    in_order_traversal(node.left, array)
    array.append(node)
    in_order_traversal(node.right, array)

    return array
