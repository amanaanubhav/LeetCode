class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        words = s.split()
        lastword=words[-1]
        length=len(lastword)

        return length

