class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0 
        
        # loop through the grid 
        for i in range(0, len(grid)): 
            for j in range(0, len(grid[i])): 
                # If we encounter an island, we increment
                if(grid[i][j] is "1"): 
                    count += 1           
                    # We try to find all adjacent land 
                    self.DFS(i, j, grid)
                    
        return count 
            
    def DFS(self, i, j, grid): 
        # Check if it's in illegal position or not 
        if(i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] is "0"): 
            return
        
        # Check neighbours 
        grid[i][j] = "0"
        self.DFS(i - 1, j, grid)
        self.DFS(i + 1, j, grid)
        self.DFS(i, j -1, grid)
        self.DFS(i, j + 1, grid)