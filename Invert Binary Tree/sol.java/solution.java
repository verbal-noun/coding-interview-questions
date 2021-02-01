public class TreeNode { 
    TreeNode left;
    TreeNode right; 
    int val;  

    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val; 
        this.left = left; 
        this.right = right; 
    }
    
}

public class solution {
    public TreeNode invertTree(TreeNode root) { 
        if(root == null) {
            return null; 
        }
        
        TreeNode left = invertTree(root.left); 
        TreeNode right = invertTree(root.right); 
        root.left = right; 
        root.right = left; 
        
        return root; 
    }
    
}


