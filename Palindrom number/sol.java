class Solution {
    public boolean isPalindrome(int x) {
      
      if(x < 0) {
        return false; 
      }
      
      if(x <= 9) {
        return true; 
      }
      
      int num = x;
      int rev = 0, rem = 0; 
      
      while(num != 0) {
        rem = num % 10; 
        rev = rev * 10 + rem; 
        num /= 10; 
      }
      
      if(rev == x){
        return true;
      } else {
        return false; 
      }
    }
  }