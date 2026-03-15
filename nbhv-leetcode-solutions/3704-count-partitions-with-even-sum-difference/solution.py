class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        
        left_sum = 0
        partitions_count = 0

        for i in range(len(nums) - 1):
            left_sum += nums[i]
            
            right_sum = total_sum - left_sum
            
            if (left_sum - right_sum) % 2 == 0:
                partitions_count += 1
                
        return partitions_count
