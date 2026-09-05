class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(0,k+1):
            heapq.heappop(nums)
        return nums[0]
        