class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1

        # Sort by frequency (highest first) and pick top k
        sorted_hashmap = sorted(hashmap, key=lambda x: hashmap[x], reverse=True)

        return sorted_hashmap[:k]  # return top k elements