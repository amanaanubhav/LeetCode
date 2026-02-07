class Solution:
    def reverse(self, x: int) -> int:

        MIN_INT, MAX_INT = -2147483648, 2147483647
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        reversed_num = 0
        
        while x != 0:
            digit = x % 10
            x //= 10
            if reversed_num > (MAX_INT - digit) // 10:
                return 0
                
            reversed_num = (reversed_num * 10) + digit
            
        return reversed_num * sign
