'''
Time complexity : O(d) - d is the number of digits in the number 
'''
class Solution:
    def isPalindrome(self, x):
        '''
        :type x: int
        :rtype: bool
        '''
        if(x < 0):
            return False 
            
        if(x <= 9):
            return True 
            
        rev = 0
        num = x 
        while(num != 0): 
            rem = num % 10 
            rev = rev * 10 + rem 
            num = num // 10 
            
        if(rev == x):
            return True
        else: 
            return False 
