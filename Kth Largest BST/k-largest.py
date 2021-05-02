# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    # Write your code here.
    sorted_values = []
    in_order_traversal(tree, sorted_values)
    return sorted_values[len(sorted_values) - k]


def in_order_traversal(node, sorted_values):
    # Base case
    if node is None:
        return
    # left
    in_order_traversal(node.left, sorted_values)
    # Self
    sorted_values.append(node.value)
    # Right
    in_order_traversal(node.right, sorted_values)
