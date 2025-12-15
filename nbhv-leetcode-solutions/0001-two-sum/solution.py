class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numHashMap={}
        for i, num in enumerate(nums):
            numHashMap[num]=i
        for i, num in enumerate(nums):
            diff = target - num
            if diff in numHashMap:
                diffIndex=numHashMap[diff]
                if diffIndex!=i:
                    return[i, diffIndex]
                
