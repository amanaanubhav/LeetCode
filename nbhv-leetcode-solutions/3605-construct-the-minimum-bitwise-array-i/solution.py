class Solution:
    # Ensure this name matches the problem exactly
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        ans = []
        for target in nums:
            found = False
            for x in range(target):
                if (x | (x + 1)) == target:
                    ans.append(x)
                    found = True
                    break
            if not found:
                ans.append(-1)
        return ans
