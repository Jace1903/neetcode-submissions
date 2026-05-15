class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:              # ✅ indented correctly
            n = n & (n - 1)
            count += 1
        return count