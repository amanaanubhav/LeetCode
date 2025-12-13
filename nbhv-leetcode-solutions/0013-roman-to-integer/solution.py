class Solution:
    def romanToInt(self, s: str) -> int:
        d={'I':1 , 'V':5 , 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        sum=0
        length=len(s)
        l=0
        while(l<length):
            if l<length-1 and d[s[l]]<d[s[l+1]]:
                sum += d[s[l+1]]-d[s[l]]
                l+=2
            else:
                sum += d[s[l]]
                l+=1
        return sum

        
