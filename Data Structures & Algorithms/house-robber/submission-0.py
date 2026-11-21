class Solution:
    def rob(self, nums: list[int]) -> int:
        prev2, prev1 = 0, 0          # go(i-2), go(i-1)
        for x in nums:
            prev2, prev1 = prev1, max(prev1, x + prev2)
        return prev1

        