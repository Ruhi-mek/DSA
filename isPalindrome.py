class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False 
        pre_x = x
        rev_x = 0
        while x > 0:
            rem = x % 10
            rev_x = rev_x*10 + rem
            x = x // 10
        if pre_x == rev_x:
            return  True
        else:
            return False    
