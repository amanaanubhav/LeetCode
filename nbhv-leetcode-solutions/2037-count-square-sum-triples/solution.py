import math

class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c_squared = a**2 + b**2
                
                c = math.isqrt(c_squared)
                
                if c <= n and c * c == c_squared:
                    count += 1
                    
        return count
