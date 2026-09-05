class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap=[-n for n in nums]
        heapq.heapify(max_heap)
        for i in range(0,k+1):
            heapq.heappop(nums)
        return nums[0]
        