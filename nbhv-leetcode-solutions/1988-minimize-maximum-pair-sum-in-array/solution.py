class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        # Sort array -> the greedy strategy
        nums.sort()
        
        max_sum = 0
        left = 0
        right = len(nums) - 1
        
        # two pointers to pair the smallest with the largest
        while left < right:
            current_pair_sum = nums[left] + nums[right]
            
            # Update the maximum pair sum found so far
            if current_pair_sum > max_sum:
                max_sum = current_pair_sum
            
            # Move pointers toward the center
            left += 1
            right -= 1
            
        return max_sum
