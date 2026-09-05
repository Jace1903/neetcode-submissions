class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap=[-n for n in nums]
        heapq.heapify(max_heap)
        for i in range(1,k):
            heapq.heappop(max_heap)
        return -max_heap[0]
        