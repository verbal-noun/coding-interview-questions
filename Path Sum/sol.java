/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        
        return traverseTree(root, targetSum);
    }
    
    private Boolean traverseTree(TreeNode node, int currentSum) {
        if(node == null) {
            return false; 
        }
        
        int newSum = currentSum - node.val; 
        if(node.left == null && node.right == null && newSum == 0) {
            return true;
        }
        
        return traverseTree(node.left, newSum) || traverseTree(node.right, newSum);
    }
}