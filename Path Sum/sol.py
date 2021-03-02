# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        return self.traverse_tree(root, targetSum)
        
    def traverse_tree(self, node, current_sum): 
        if node is None: 
            return False 
        
        new_sum = current_sum - node.val
        if(node.left is None and node.right is None and  new_sum == 0):
            return True 
        
        return self.traverse_tree(node.left, new_sum) or self.traverse_tree(node.right, new_sum)