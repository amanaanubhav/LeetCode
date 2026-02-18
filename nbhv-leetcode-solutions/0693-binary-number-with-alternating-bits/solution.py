class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = f"{n:b}" 
        
        for i in range (len(binary) - 1):
            if binary[i] == binary[i+1]:
                return False

        else:
            return True


