# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # Check the root
        return self.traverse(root, subRoot)

    def equals(self, node, target):
        # Base cases
        if(node is None or target is None):
            return node is None and target is None

        # Usual case
        # Check if descendents match or not
        return node.val == target.val and self.equals(node.left, target.left) and self.equals(node.right, target.right)

    def traverse(self, node, sub_root):
        if node is None:
            return False

        return self.equals(node, sub_root) or self.traverse(node.left, sub_root) or self.traverse(node.right, sub_root)


"""
 - For each node I try to match the sub current node 
 
 - Pass the matcher to the descendents 
 
 - Do the root finding and subtree matching simultaneously 
 
 - 
 
 
          -> 3 
            
         4       5
        
        
    1       2 
    
"""
