import heapq

# This is an input class. Do not edit.


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, num_of_visited_nodes, last_visited):
        self.num_of_visited_nodes = num_of_visited_nodes
        self.last_visited = last_visited


def findKthLargestValueInBst(tree, k):
    # Write your code here.
    tree_info = TreeInfo(0, -1)
    reverse_inorder_traversal(tree, k, tree_info)
    return tree_info.last_visited


def reverse_inorder_traversal(node, target, tree_info):
    # Base case
    if node is None or tree_info.num_of_visited_nodes > target:
        return

    # right
    reverse_inorder_traversal(node.right, target, tree_info)
    # Self or left
    if tree_info.num_of_visited_nodes < target:
        tree_info.num_of_visited_nodes += 1
        tree_info.last_visited = node.value
        reverse_inorder_traversal(node.left, target, tree_info)
