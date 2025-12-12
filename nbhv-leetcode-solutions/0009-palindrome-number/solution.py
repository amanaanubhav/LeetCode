class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reversed_num = 0
        temp = x
        
        while temp > 0:
            digit = temp % 10
            reversed_num = (reversed_num * 10) + digit

            temp = temp // 10
            
        return x == reversed_num
