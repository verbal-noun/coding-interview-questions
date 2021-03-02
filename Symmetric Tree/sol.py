# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root, root)
    
    
    def isMirror(self, left, right): 
        # If both tree is null return true 
        if(left == None and right == None):
            return True
        
        # If any one of the trees are not null, return false 
        if(left == None or right == None): 
            return False 
        
        # Else check if the values match and check their children recursively 
        return (left.val == right.val) and self.isMirror(left.right, right.left) and self.isMirror(left.left, right.right)