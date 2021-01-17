import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public List<List<Integer>> threeSum(int[] A) {
        // Sorting the initial array 
        Arrays.sort(A); 
        // Creating a hashset to hold seen triplets 
        Set<List<Integer>> allThreeSums = new HashSet<>(); 
        int secondLastIndex = A.length - 2;

        for(int i = 0; i < secondLastIndex; i++) {
            findTwoSum(i, A, allThreeSums); 
        }

        return new ArrayList<>(allThreeSums); 
    }

    private void findTwoSum(int rootIndex, int[] A, Set<List<Integer>> allThreeSums) {
        int left = rootIndex + 1; 
        int right = A.length - 1; 

        while (left < right) {
            int threeNumberSum = A[rootIndex] + A[right] + A[left]; 

            if(threeNumberSum == 0) {
                allThreeSums.add(Arrays.asList(A[rootIndex], A[left], A[right]));
                left++; 
                right--;

            } else if (threeNumberSum < 0) {
                left++;
            } else {
                right--; 
            }
        }
    }
}