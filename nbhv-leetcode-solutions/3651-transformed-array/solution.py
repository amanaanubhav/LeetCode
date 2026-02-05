class Solution:
    def constructTransformedArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        
        for i in range(n):
            steps = nums[i]
            target_index = (i + steps) % n
            
            result[i] = nums[target_index]
            
        return result
