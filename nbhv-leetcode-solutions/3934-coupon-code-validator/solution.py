class Solution:
    def validateCoupons(self, code: list[str], businessLine: list[str], isActive: list[bool]) -> list[str]:
        priority = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }
        
        valid_coupons = []
        
        # Filtering Phase
        for i in range(len(code)):
            c = code[i]
            b = businessLine[i]
            active = isActive[i]
            
            if not active:
                continue
            
            if b not in priority:
                continue
            
            if not c or not all(char.isalnum() or char == '_' for char in c):
                continue
                
            # If all checks pass, store the data needed for sorting
            valid_coupons.append((b, c))
            
        valid_coupons.sort(key=lambda x: (priority[x[0]], x[1]))
        
        return [coupon[1] for coupon in valid_coupons]
