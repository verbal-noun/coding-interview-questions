# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, balanced, height):
        self.balanced = balanced
        self.height = height


def heightBalancedBinaryTree(tree):
    # Write your code here.
    tree_info = get_tree_info(tree)

    return tree_info.balanced


def get_tree_info(node):

    # Base cases
    if node is None:
        return TreeInfo(True, -1)

    # Usual cases
    left_subtree = get_tree_info(node.left)
    right_subtree = get_tree_info(node.right)

    balanced = (left_subtree.balanced and
                right_subtree.balanced and
                abs(left_subtree.height - right_subtree.height) <= 1
                )

    height = max(left_subtree.height, right_subtree.height) + 1

    return TreeInfo(balanced, height)


"""
- For each node, check the height of left subtree and right subtree 
- current height will be passed in each node 

- traverse the nodes 
- Caculate height of left subtree, right subtree 
- compare the and return 
- return current, left and right child's result

o(n * n) 

- state and height at the same time 
- (tuple), tree_info -> class 

- Traverse trought the nodes 
- if any of the child is imbalance -> imbalance 
- Calculate the height for the sake of calcuting 
- return the state(height and balanced)

o(n) 

"""
