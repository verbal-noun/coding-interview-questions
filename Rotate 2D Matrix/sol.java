class Solution {
    public int[][] rotate(int[][] matrix) {
      // Figure out the size of the matrix 
      int size = matrix.length - 1; 
    
      // Loop through layer by layer 
      for(int layer = 0; layer < matrix.length / 2; layer++) {
        for(int i = layer; i < size - layer; i++) {
          // Determine the corners 
          int top_corner = matrix[layer][i];
          int right_corner = matrix[i][size-layer]; 
          int bottom_corner = matrix[size - layer][size - i]; 
          int left_corner = matrix[size - i][layer]; 
          
          // Change the corners in each layer 
          matrix[layer][i] = left_corner; 
          matrix[i][size-layer] = top_corner; 
          matrix[size - layer][size - i] = right_corner; 
          matrix[size - i][layer] = bottom_corner; 
        }
      }  
      
      return matrix; 
    }
  }